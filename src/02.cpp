#include <iostream>
#include <sstream>
#include <vector>
#include <functional>

#include "common/common.h"

struct Command {
    const std::string direction;
    const int value;
};

std::pair<int, int> solve(const std::vector<Command> &commands) {
    int hpos = 0;
    int depth_1 = 0;
    int depth_2 = 0;
    int aim = 0;
    for (const auto &command : commands) {
        if (command.direction == "forward") {
            hpos += command.value;
            depth_2 += aim * command.value;
        }
        else if (command.direction == "up") {
            depth_1 -= command.value;
            aim -= command.value;
        }
        else if (command.direction == "down") {
            depth_1 += command.value;
            aim += command.value;
        }
    }
    return std::pair(hpos * depth_1, hpos * depth_2);
}

Command parse(std::string line) {
    std::stringstream lineStream{line};

    std::string direction;
    lineStream >> direction;

    int value;
    lineStream >> value;

    return { direction, value };
}

int main(int argc, char** argv) {
    std::function<Command (std::string)> f = parse;
    std::vector<Command> commands = getParsedLines(argv[1], f);
    std::cout << solve(commands).first << std::endl;
    std::cout << solve(commands).second << std::endl;
}
