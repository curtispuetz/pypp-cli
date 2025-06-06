#include "src/first.h"
#include "src/fourth.h"
#include "src/second.h"
#include "src/third.h"
#include <iostream>
#include <string>

int main() {
    std::cout << return_something(1, 9) << std::endl;
    std::cout << return_friend() << std::endl;
    std::cout << using_inline_string() << std::endl;
    std::string input = "a";
    std::string result = string_as_argument(input);
    input = "b";
    std::cout << result << std::endl;
    std::cout << input << std::endl;
    return 0;
}