#pragma once

#include <iostream>
#include <sstream>
#include <type_traits>
#include <variant>

namespace pypp {
template <typename... Types> class Uni {
  public:
    using VariantType = std::variant<Types...>;

    // Delete default constructor to require a value
    Uni() = delete;
    Uni(const Uni &) = delete;
    Uni &operator=(const Uni &) = delete;
    Uni(Uni &&) = default;
    Uni &operator=(Uni &&) = default;

    template <typename T, typename = std::enable_if_t<
                              (std::disjunction_v<std::is_same<T, Types>...>)>>
    explicit Uni(T &&value) : data_(std::move(value)) {}

    // Check if the stored value is of type T
    template <typename T> bool isinst() const {
        return std::holds_alternative<T>(data_);
    }

    bool is_none() const {
        return std::holds_alternative<std::monostate>(data_);
    }

    // Get value as T (throws if wrong type)
    template <typename T> T &ug() { return std::get<T>(data_); }

    bool operator==(const Uni &other) const { return data_ == other.data_; }
    bool operator!=(const Uni &other) const { return !(*this == other); }

    void print(std::ostream &os) const {
        std::visit([&os](const auto &value) { os << "Union[" << value << "]"; },
                   data_);
    }

    void print() const {
        print(std::cout);
        std::cout << std::endl;
    }

  private:
    VariantType data_;
};

template <typename... Types>
std::ostream &operator<<(std::ostream &os, const pypp::Uni<Types...> &u) {
    u.print(os);
    return os;
}

// deduction guide
template <typename... Ts> Uni(Ts...) -> Uni<Ts...>;
} // namespace pypp
