#include <iostream>
#include <fstream>
#include <vector>
#include <functional>

#include "common/common.h"

using namespace std;

const auto HUGE = 99999l;

long solve_1(vector<long> numbers) {
    auto previous = HUGE;
    auto result = 0l;
    for (long n : numbers) {
        if (n > previous) {
            ++result;
        }
        previous = n;
    }
    return result;
}

long solve_2(vector<long> numbers) {
    long p_1 = HUGE, p_2 = HUGE, p_3 = HUGE;
    long result = 0l;
    for (long n : numbers) {
        if (n + p_1 + p_2 > p_1 + p_2 + p_3) {
            ++result;
        }
        p_3 = p_2;
        p_2 = p_1;
        p_1 = n;
    }
    return result;
}

int main(int argc, char** argv)
{
    function<long(string)> parse = [](string s) {return stoi(s);};
    vector<long> numbers = getParsedLines(argv[1], parse);
    cout << solve_1(numbers) << endl;
    cout << solve_2(numbers) << endl;
}
