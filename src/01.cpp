#include <iostream>
#include <vector>

#include "common/common.h"

const int HUGE = 99999;

int solve_1(const std::vector<int> &numbers) {
    int previous = HUGE;
    int result = 0l;
    for (const int n : numbers) {
        if (n > previous) {
            ++result;
        }
        previous = n;
    }
    return result;
}

int solve_2(const std::vector<int> &numbers) {
    int p_1 = HUGE, p_2 = HUGE, p_3 = HUGE;
    int result = 0l;
    for (const auto n : numbers) {
        if (n + p_1 + p_2 > p_1 + p_2 + p_3) {
            ++result;
        }
        p_3 = p_2;
        p_2 = p_1;
        p_1 = n;
    }
    return result;
}

int main(int argc, char** argv) {
    parse_fn<int> parse = [](const std::string &s) {return std::stoi(s);};
    const auto numbers = getParsedLines(argv[1], parse);
    std::cout << solve_1(numbers) << std::endl;
    std::cout << solve_2(numbers) << std::endl;
}
