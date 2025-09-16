// A wrapper around std::vector without any methods
#pragma once

#include "py_list.h"
#include <vector>

template <typename T>
class PseudoSubscriptableTypeCpp
{
public:
    std::vector<T> data_;
    PseudoSubscriptableTypeCpp(int size) : data_(size) {}
    void print() const
    {
        // Just to have a method that can be called
        std::cout << "easter egg" << std::endl;
    }
};

template <typename T>
class PseudoSubscriptableType2Cpp
{
public:
    pypp::PyList<T> data_;
    PseudoSubscriptableType2Cpp(pypp::PyList<T> vec) : data_(std::move(vec)) {}
    void print() const
    {
        // Just to have a method that can be called
        std::cout << "easter egg" << std::endl;
    }
};

// Deduction guide
template <typename T>
PseudoSubscriptableType2Cpp(pypp::PyList<T>) -> PseudoSubscriptableType2Cpp<T>;
