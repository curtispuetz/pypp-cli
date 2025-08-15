// A wrapper around std::vector without any methods
#pragma once
#include <vector>
#include "py_list.h"

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
    PyList<T> data_;
    PseudoSubscriptableType2Cpp(PyList<T> vec) : data_(std::move(vec)) {}
    void print() const
    {
        // Just to have a method that can be called
        std::cout << "easter egg" << std::endl;
    }
};

// Deduction guide
template <typename T>
PseudoSubscriptableType2Cpp(PyList<T>) -> PseudoSubscriptableType2Cpp<T>;
