#include "constants.h"
#include "compy_util/print.h"

const int _A = 2;
struct _PseudoCompyName_PrivateConfig {
    int a = 1;
    int b = 2;
};
inline _PseudoCompyName_PrivateConfig _PrivateConfig;

void constant_fn() {
    print(PyStr("CONSTANT RESULTS:"));
    const int _F = 4;
    print(F);
    print(_F);
    print(G(1));
    print(MyConfig.a, MyConfig.b);
    print(MyConfig2.a, MyConfig2.b);
    print(_PrivateConfig.a, _PrivateConfig.b);
}
