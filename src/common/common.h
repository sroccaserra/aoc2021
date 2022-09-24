#ifndef COMMON_H
#define COMMON_H

#include <vector>
#include <string>
#include <fstream>

template<typename T>
using parse_fn = T(*)(const std::string&);

template<typename T>
std::vector<T> getParsedLines(char* filename, parse_fn<T> parse) {
    std::ifstream infile(filename);
    std::vector<T> numbers = {};
    for (std::string line; std::getline(infile, line); ) {
        numbers.emplace_back(parse(line));
    }
    return numbers;
}

#endif // COMMON_H
