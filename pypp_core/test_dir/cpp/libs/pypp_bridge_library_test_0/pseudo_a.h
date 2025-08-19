#pragma once

namespace test_namespace
{
    class PseudoACpp
    {
    public:
        int a_;
        explicit PseudoACpp(int a) : a_(a) {}
        int get_a() const { return a_; }
    };
}