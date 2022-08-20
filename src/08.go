package main

import (
	"fmt"
	"strings"

	. "aoc2021/src/common"
)

func solve_08(entries []entry) int {
	var searched = map[int]bool{
		2: true,
		3: true,
		4: true,
		7: true,
	}

	var n = 0
	for _, entry := range entries {
		for _, digit := range entry.output {
			if searched[len(digit)] {
				n += 1
			}
		}
	}
	return n
}

type entry struct {
	signals []string
	output  []string
}

func parseLine(line string) entry {
	var parts = strings.Split(line, " | ")
	return entry{
		strings.Split(parts[0], " "),
		strings.Split(parts[1], " "),
	}
}
func main() {
	lines := GetParsedLines(parseLine)
	fmt.Println(solve_08(lines))
}
