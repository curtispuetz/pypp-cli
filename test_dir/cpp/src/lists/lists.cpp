#include "lists\lists.h"

PyStr list_fn() {
    std::vector<int> my_list = {1, 2, 3, 4, 5};
    my_list[0] = 10;
    my_list.push_back(11);
    return to_pystr(my_list[-1]);
}