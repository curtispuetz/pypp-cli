#include "classes/more_tests.h"

class _PrivateClass {
  public:
    int xyz;
    _PrivateClass(int a_abc) : xyz(std::move(a_abc)) {}
};
