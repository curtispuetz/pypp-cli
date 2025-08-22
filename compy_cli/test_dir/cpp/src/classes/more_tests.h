#pragma once

#include <utility>

class ClassA {
  public:
    int _x;
    int _y;
    int _z;
    ClassA(int a_x, int a_y, int a_z)
        : _x(std::move(a_x)), _y(std::move(a_y)), _z(std::move(a_z)) {}
};

class ClassWithDifferentOrder {
  public:
    int _z;
    int _x;
    int _y;
    ClassWithDifferentOrder(int a_x, int a_y, int a_z)
        : _z(std::move(a_z)), _x(std::move(a_x)), _y(std::move(a_y)) {}
};
