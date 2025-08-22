#pragma once
#include <type_traits>
#include <variant>

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

  private:
    VariantType data_;
};

// dedction guide
template <typename... Ts> Uni(Ts...) -> Uni<Ts...>;