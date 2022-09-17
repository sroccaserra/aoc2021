#ifndef COMMON_H
#define COMMON_H

#include <vector>
#include <string>
#include <fstream>
#include <functional>

template<typename T>
std::vector<T> getParsedLines(char* filename, std::function<T (std::string)> parse_fn) {
    std::ifstream infile(filename);
    std::vector<T> numbers = {};
    for (std::string line; std::getline(infile, line); ) {
        numbers.emplace_back(parse_fn(line));
    }
    return numbers;
}

#endif // COMMON_H
