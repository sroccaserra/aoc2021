package main

import (
	"fmt"
	"strings"

	. "aoc2021/src/common"
)

func solve_08_1(entries []entry) int {
	var searched = map[int]bool{2: true, 3: true, 4: true, 7: true}
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

func solve_08_2(entries []entry) int {
	var result = 0
	for _, entry := range entries {
		var segmentsForOne, segmentsForFour = findReferences(entry.signals)
		var number = 0
		for _, digit := range entry.output {
			number = 10*number + findDigitValue(segmentsForOne, segmentsForFour, digit)
		}
		result += number
	}
	return result
}

func findReferences(signals []string) (string, string) {
	var segmentsForOne, segmentsForFour string
	for _, signal := range signals {
		if len(signal) == 2 {
			segmentsForOne = signal
		}
		if len(signal) == 4 {
			segmentsForFour = signal
		}
	}
	return segmentsForOne, segmentsForFour
}

func findDigitValue(segmentsForOne, segmentsForFour, digit string) int {
	var knownValues = map[int]int{2: 1, 3: 7, 4: 4, 7: 8}
	var nbSegments = len(digit)
	if result, ok := knownValues[nbSegments]; ok {
		return result
	}
	if nbSegments == 5 {
		return findTwoThreeOrFive(segmentsForOne, segmentsForFour, digit)
	}
	return findZeroSixOrNine(segmentsForOne, segmentsForFour, digit)
}

func findTwoThreeOrFive(segmentsForOne, segmentsForFour, digit string) int {
	if countSuperimposedSegments(segmentsForFour, digit) == 7 {
		return 2
	}
	if countSuperimposedSegments(segmentsForOne, digit) == len(digit) {
		return 3
	}
	return 5
}

func findZeroSixOrNine(segmentsForOne, segmentsForFour, digit string) int {
	if countSuperimposedSegments(segmentsForFour, digit) == len(digit) {
		return 9
	}
	if countSuperimposedSegments(segmentsForOne, digit) == len(digit) {
		return 0
	}
	return 6
}

func countSuperimposedSegments(lhs, rhs string) int {
	result := len(lhs)
	for _, v := range rhs {
		if !strings.ContainsRune(lhs, v) {
			result++
		}
	}
	return result
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
	fmt.Println(solve_08_1(lines))
	fmt.Println(solve_08_2(lines))
}
