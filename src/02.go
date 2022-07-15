package main

import (
	"fmt"
	"strconv"
	"strings"

	"aoc2021/src/common"
)

func solve_02(commands []command) (int, int) {
	var hpos, depth_1, depth_2, aim int
	for _, command := range commands {
		switch command.direction {
		case "forward":
			hpos += command.value
			depth_2 += aim * command.value
		case "up":
			depth_1 -= command.value
			aim -= command.value
		case "down":
			depth_1 += command.value
			aim += command.value
		}
	}
	return hpos * depth_1, hpos * depth_2
}

func parse(line string) command {
	parts := strings.Fields(line)
	direction := parts[0]
	value, _ := strconv.Atoi(parts[1])
	return command{direction, value}
}

type command struct {
	direction string
	value     int
}

func main() {
	commands := common.GetParsedLines(parse)
	solution_1, solution_2 := solve_02(commands)
	fmt.Println(solution_1)
	fmt.Println(solution_2)
}
