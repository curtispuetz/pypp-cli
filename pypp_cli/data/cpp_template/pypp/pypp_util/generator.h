// TODO later: I will need this generator later likely for some stuff, but it is
// unused right now
//  Example usage this (it works very much like Python):
// Generator<int> compute_slice_indices(int start, int stop, int step, int n) {
//    if (stop == NULL) stop = n;
//    if (start < 0) start += n;
//    if (stop < 0) stop += n;
//
//    if (start < 0) start = 0;
//    if (stop > n) stop = n;
//
//    if (step > 0 && start < stop) {
//        for (int i = start; i < stop; i += step)
//            co_yield i;
//    } else if (step < 0 && start > stop) {
//        for (int i = start; i > stop; i += step)
//            co_yield i;
//    }
//}
#pragma once

#include <coroutine>
#include <exception>

#define PYPP_CO_YIELD_FROM(gen)                                                \
    for (auto &&_v : (gen))                                                    \
    co_yield std::move(_v)

namespace pypp {

template <typename T> struct Generator {
    struct promise_type {
        T current_value;

        Generator get_return_object() {
            return Generator{
                std::coroutine_handle<promise_type>::from_promise(*this)};
        }

        std::suspend_always initial_suspend() { return {}; }

        std::suspend_always final_suspend() noexcept { return {}; }

        std::suspend_always yield_value(T value) {
            current_value = value;
            return {};
        }

        void return_void() {}

        void unhandled_exception() { std::terminate(); }
    };

    using handle_type = std::coroutine_handle<promise_type>;

    explicit Generator(handle_type h) : coro(h) {}
    Generator(const Generator &) = delete;
    Generator &operator=(const Generator &) = delete;
    Generator(Generator &&other) noexcept : coro(other.coro) {
        other.coro = nullptr;
    }

    ~Generator() {
        if (coro)
            coro.destroy();
    }

    struct iterator {
        handle_type coro;

        iterator() : coro(nullptr) {}
        explicit iterator(handle_type h) : coro(h) {}

        iterator &operator++() {
            coro.resume();
            if (coro.done())
                coro = nullptr;
            return *this;
        }

        T operator*() const { return coro.promise().current_value; }

        bool operator!=(const iterator &rhs) const { return coro != rhs.coro; }
    };

    iterator begin() {
        if (coro) {
            coro.resume();
            if (coro.done())
                return iterator{nullptr};
        }
        return iterator{coro};
    }

    iterator end() { return iterator{nullptr}; }

  private:
    handle_type coro;
};

} // namespace pypp