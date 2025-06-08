#include "lists\lists.h"

int list_fn() {
    std::vector<int> my_list = {1, 2, 3, 4, 5};
    my_list[0] = 10;
    my_list.push_back(11);
    return my_list[-1];
}