#pragma once

#include <iterator>
#include <tuple> // Use std::tuple instead of PyTup
#include <utility>

namespace pypp {
// Forward declaration of the iterator class
template <typename... Iterators> class py_zip_iterator;

// The main PyZip class (the "range")
// Uses variadic templates to accept any number of containers
template <typename... T> class PyZip {
  public:
    // Constructor uses universal references to handle both lvalues and rvalues
    PyZip(T &&...iterables) : _iterables(std::forward<T>(iterables)...) {}

    // The begin() method returns our custom iterator.
    // It creates a zip iterator from the begin() iterator of each container.
    auto begin() {
        // std::apply unpacks the tuple of containers and passes each as an
        // argument to the lambda, which then calls std::begin on each one.
        return std::apply(
            [](auto &&...args) { return py_zip_iterator(std::begin(args)...); },
            _iterables);
    }

    // The end() method works similarly.
    // It creates a zip iterator from the end() iterator of each container.
    // The comparison logic in the iterator itself will handle stopping at the
    // shortest sequence.
    auto end() {
        return std::apply(
            [](auto &&...args) { return py_zip_iterator(std::end(args)...); },
            _iterables);
    }

  private:
    // A tuple to hold all the containers passed to the constructor.
    std::tuple<T...> _iterables;
};

// C++17 Deduction Guide for easier instantiation (e.g., PyZip(vec1, list2))
template <typename... T> PyZip(T &&...) -> PyZip<T...>;

// The iterator for PyZip
template <typename... Iterators> class py_zip_iterator {
  private:
    // Helper to get the reference type from an iterator (e.g., int& from
    // vector<int>::iterator)
    template <typename Iter>
    using reference_t = typename std::iterator_traits<Iter>::reference;

  public:
    // --- C++ Standard Iterator Traits ---
    using iterator_category = std::input_iterator_tag;
    // The value_type is a std::tuple of the value_types of the underlying
    // iterators
    using value_type =
        std::tuple<typename std::iterator_traits<Iterators>::value_type...>;
    // The reference type is a std::tuple of references from the underlying
    // iterators
    using reference = std::tuple<reference_t<Iterators>...>;
    using difference_type = std::ptrdiff_t;
    using pointer = void;
    // --- End of Traits ---

    // Constructor takes one iterator for each container
    py_zip_iterator(Iterators... its) : _its(its...) {}

    // Dereference operator (*it)
    // Returns a std::tuple containing references to the elements from each
    // container.
    reference operator*() const {
        // Use std::apply to unpack the tuple of iterators and pass them to a
        // lambda
        return std::apply(
            // The lambda takes each iterator and dereferences it (*arg)
            [](auto &&...args) {
                // This creates the std::tuple on the fly: std::tuple<int&,
                // std::string&,
                // ...>
                return reference(*args...);
            },
            _its);
    }

    // Pre-increment operator (++it)
    // Increments each of the underlying iterators.
    py_zip_iterator &operator++() {
        // Use std::apply with a fold expression to increment every iterator in
        // the tuple
        std::apply([](auto &&...args) { ((++args), ...); }, _its);
        return *this;
    }

    // Comparison operator (it != end())
    // The zip operation should stop when ANY of the iterators reaches its end.
    // Therefore, we check that ALL of the iterators are not equal to their
    // corresponding 'end' iterators.
    bool operator!=(const py_zip_iterator &other) const {
        // We use a helper lambda and an index sequence to compare each element
        // of our iterator tuple with the corresponding element in the other
        // tuple.
        return compare_all_not_equal(other,
                                     std::index_sequence_for<Iterators...>{});
    }

  private:
    // A tuple to hold the current iterator for each container
    std::tuple<Iterators...> _its;

    // Helper function for the comparison operator
    template <std::size_t... I>
    bool compare_all_not_equal(const py_zip_iterator &other,
                               std::index_sequence<I...>) const {
        // C++17 fold expression: expands to
        // (get<0>(_its) != get<0>(other._its)) && (get<1>(_its) !=
        // get<1>(other._its)) && ...
        return ((std::get<I>(_its) != std::get<I>(other._its)) && ...);
    }
};

} // namespace pypp
