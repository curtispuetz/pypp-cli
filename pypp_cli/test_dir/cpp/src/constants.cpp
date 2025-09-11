#include "constants.h"
#include "pypp_util/print.h"

namespace me {
const int _A = 2;
struct __PseudoPyppName_PrivateConfig {
    int a = 1;
    int b = 2;
};
inline __PseudoPyppName_PrivateConfig _PrivateConfig;

void constant_fn() {
    pypp::print(pypp::PyStr("CONSTANT RESULTS:"));
    const int _F = 4;
    pypp::print(F);
    pypp::print(_F);
    pypp::print(G(1));
    pypp::print(MyConfig.a, MyConfig.b);
    pypp::print(MyConfig2.a, MyConfig2.b);
    pypp::print(_PrivateConfig.a, _PrivateConfig.b);
}

} // namespace me