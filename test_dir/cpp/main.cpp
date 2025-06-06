#include "src/first.h"
#include "src/fourth.h"
#include "src/second.h"
#include "src/third.h"
#include <iostream>

int main() {
    std::cout << return_something(1, 9) << std::endl;
    std::cout << return_friend() << std::endl;
    std::cout << using_inline_string() << std::endl;
    std::cout << string_as_argument("hello") << std::endl;
    return 0;
}