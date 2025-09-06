#include "first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_bridge_library_test_0/pseudo_custom_type_cpp.h"
#include "pypp_util/print.h"

void first_fn()
{
  pypp::print(pypp::PyStr("Hello from first_fn()"));
  pypp::PyList<int> a = pypp::PyList({1, 2, 3});
  pypp::print(a);
  pypp::print(&a);
  PseudoCustomTypeCpp b = PseudoCustomTypeCpp(1);
  pypp::print(&b);
}
