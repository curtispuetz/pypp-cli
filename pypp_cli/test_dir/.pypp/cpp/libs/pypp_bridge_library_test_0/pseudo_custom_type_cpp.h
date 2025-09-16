#pragma once

class PseudoCustomTypeCpp
{
public:
    int a_;
    explicit PseudoCustomTypeCpp(int a) : a_(a) {}
    int get_a() const { return a_; }
};
