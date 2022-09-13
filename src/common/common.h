#ifndef COMMON_H
#define COMMON_H

#include <vector>
#include <string>

template<typename T>
std::vector<T> getParsedLines(char* filename, std::function<T (std::string)> parse_fn) {
    std::ifstream infile(filename);
    std::vector<T> numbers = {};
    std::string line;
    while (infile >> line) {
        numbers.push_back(parse_fn(line));
    }
    return numbers;
}

#endif // COMMON_H
