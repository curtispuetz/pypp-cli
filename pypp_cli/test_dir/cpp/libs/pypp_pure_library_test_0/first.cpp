#include "first.h"
#include "pypp_bridge_library_test_0/pseudo_custom_type_cpp.h"
#include "pypp_util/print.h"
#include "py_list.h"
#include "py_str.h"

void first_fn()
{
  print(PyStr("Hello from first_fn()"));
  PyList<int> a = PyList({1, 2, 3});
  print(a);
  print(&a);
  PseudoCustomTypeCpp b = PseudoCustomTypeCpp(1);
  print(&b);
}
