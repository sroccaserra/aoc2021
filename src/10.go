package main

import (
	"fmt"
	"sort"

	. "aoc2021/src/common"
)

func solve_10(lines []string) (int, int) {
	result_1 := 0
	var scores_2 []int
	for _, line := range lines {
		if firstIllegal, isCorrupted := isCorrupted(line); isCorrupted {
			result_1 += pointsForCorrupted[firstIllegal]
		} else {
			neededClosingChars := neededClosingChars(line)
			score := scoreForClosingChars(neededClosingChars)
			scores_2 = append(scores_2, score)
		}
	}
	middleIndex := len(scores_2) / 2
	sort.Ints(scores_2)
	return result_1, scores_2[middleIndex]
}

func isCorrupted(line string) (rune, bool) {
	var openingStack []rune
	for _, c := range line {
		matchingOpeningChar, isClosingChar := matchingOpeningCharFor[c]
		if isClosingChar {
			previous := Pop(&openingStack)
			if previous != matchingOpeningChar {
				return c, true
			}
		} else {
			Push(&openingStack, c)
		}
	}
	return '?', false
}

func neededClosingChars(line string) []rune {
	var result []rune
	for _, c := range line {
		matchingClosingChar, isOpeningChar := matchingClosingCharFor[c]
		if isOpeningChar {
			Push(&result, matchingClosingChar)
		} else {
			lastIndex := len(result) - 1
			if result[lastIndex] == c {
				Pop(&result)
			}
		}
	}
	return result
}

func scoreForClosingChars(closingChars []rune) int {
	result := 0
	lastIndex := len(closingChars) - 1
	for i := range closingChars {
		c := closingChars[lastIndex-i]
		result *= 5
		result += pointsForIncomplete[c]
	}
	return result
}

var matchingOpeningCharFor = map[rune]rune{
	')': '(',
	']': '[',
	'}': '{',
	'>': '<',
}

var matchingClosingCharFor = map[rune]rune{
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>',
}

var pointsForCorrupted = map[rune]int{
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
}

var pointsForIncomplete = map[rune]int{
	')': 1,
	']': 2,
	'}': 3,
	'>': 4,
}

func main() {
	lines := GetInputLines()
	result_1, result_2 := solve_10(lines)
	fmt.Println(result_1)
	fmt.Println(result_2)
}
