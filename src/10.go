package main

import (
	"fmt"

	. "aoc2021/src/common"
)

func solve_10_1(lines []string) int {
	result := 0
	for _, line := range lines {
		if firstIllegal, isCorrupted := isCorrupted(line); isCorrupted {
			result += pointsFor[firstIllegal]
		}
	}
	return result
}

func isCorrupted(line string) (rune, bool) {
	var openingStack []rune
	for _, c := range line {
		openingChar, ok := requiredOpeningChar[c]
		if !ok {
			Push(&openingStack, c)
		} else {
			previous := Pop(&openingStack)
			if previous != openingChar {
				return c, true
			}
		}
	}
	return 'x', false
}

var requiredOpeningChar = map[rune]rune{
	')': '(',
	']': '[',
	'}': '{',
	'>': '<',
}

var pointsFor = map[rune]int{
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
}

func main() {
	lines := GetInputLines()
	fmt.Println(solve_10_1(lines))
}
