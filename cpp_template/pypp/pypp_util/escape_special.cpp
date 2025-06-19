#include "pypp_util/escape_special.h"

PyStr escape_specials(const PyStr &input) {
    std::string result;
    for (char c : input.str()) {
        switch (c) {
        case '\n':
            result += "\\n";
            break;
        case '\t':
            result += "\\t";
            break;
        case '\r':
            result += "\\r";
            break;
        case '\b':
            result += "\\b";
            break;
        case '\f':
            result += "\\f";
            break;
        case '\\':
            result += "\\\\";
            break;
        case '\"':
            result += "\\\"";
            break;
        default:
            result += c;
        }
    }
    return PyStr(result);
}