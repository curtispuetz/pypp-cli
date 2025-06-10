#include <unordered_set>
#include <initializer_list>
#include <stdexcept>
#include <iostream>

template<typename T>
class PySet {
private:
    std::unordered_set<T> data;

public:
    // Constructors
    PySet() = default;
    PySet(std::initializer_list<T> init) : data(init) {}

    // Add an element
    void add(const T& value) {
        data.insert(value);
    }

    // Remove an element (raises if not found)
    void remove(const T& value) {
        auto it = data.find(value);
        if (it == data.end()) {
            throw std::runtime_error("KeyError: element not found in set");
        }
        data.erase(it);
    }

    // Discard an element (no error if not found)
    void discard(const T& value) {
        data.erase(value);
    }

    // Check membership
    bool contains(const T& value) const {
        return data.find(value) != data.end();
    }

    // Set operations
    PySet<T> union_(const PySet<T>& other) const {
        PySet<T> result = *this;
        result.data.insert(other.data.begin(), other.data.end());
        return result;
    }

    PySet<T> intersection(const PySet<T>& other) const {
        PySet<T> result;
        for (const auto& item : data) {
            if (other.contains(item)) {
                result.add(item);
            }
        }
        return result;
    }

    PySet<T> difference(const PySet<T>& other) const {
        PySet<T> result;
        for (const auto& item : data) {
            if (!other.contains(item)) {
                result.add(item);
            }
        }
        return result;
    }

    PySet<T> symmetric_difference(const PySet<T>& other) const {
        PySet<T> result;
        for (const auto& item : data) {
            if (!other.contains(item)) {
                result.add(item);
            }
        }
        for (const auto& item : other.data) {
            if (!contains(item)) {
                result.add(item);
            }
        }
        return result;
    }

    // Comparison operators (issubset, issuperset, equality)
    bool issubset(const PySet<T>& other) const {
        for (const auto& item : data) {
            if (!other.contains(item)) {
                return false;
            }
        }
        return true;
    }

    bool issuperset(const PySet<T>& other) const {
        return other.issubset(*this);
    }

    bool operator==(const PySet<T>& other) const {
        return data == other.data;
    }

    bool operator!=(const PySet<T>& other) const {
        return data != other.data;
    }

    // Size
    std::size_t len() const {
        return data.size();
    }

    // Clear
    void clear() {
        data.clear();
    }

    // Iterator support
    auto begin() const { return data.begin(); }
    auto end() const { return data.end(); }

    // For debugging
    void print() const {
        std::cout << "{";
        int i = 0;
        for (const auto& item : data) {
            std::cout << item;
            if (i != data.size() - 1) std::cout << ", ";
            i++;
        }
        std::cout << "}" << std::endl;
    }
};
