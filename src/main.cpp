#include "simple.h"
#include <array>
#include <iostream>

int main() {
    if (hard(1, 2) == 3) {
        std::cout << "simple(1, 2) == 3" << std::endl;
    }
    const size_t size = 5;
    int sum = 0;
    std::array<int, size> arr = { 1, 2, 3, 4 };
    for (const auto& iter : arr) {
        std::cout << iter << '\n';
        sum = hard(iter, sum);
        std::cout << "sum: " << sum << '\n';
    }

    // testing octo.nvim
    fprintf(stderr, "fprintf: %d\n", sum);
    return 0;
}
