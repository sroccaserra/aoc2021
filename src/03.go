package main

import (
	"fmt"

	"aoc2021/src/common"
)

func solve_03_1(report []string) int {
	nbBits := len(report[0])
	powOfTwo := 1 << (nbBits - 1)
	var gamma, epsilon int
	for i := range report[0] {
		if hasLessOrEqualZerosThanOnes(i, report) {
			gamma += powOfTwo
		} else {
			epsilon += powOfTwo
		}
		powOfTwo >>= 1
	}
	return gamma * epsilon
}

func hasLessOrEqualZerosThanOnes(i int, report []string) bool {
	var nbOnes, nbZeros int
	for _, line := range report {
		if line[i] == '0' {
			nbZeros++
		} else {
			nbOnes++
		}
	}
	return nbZeros <= nbOnes
}

func solve_03_2(report []string) int {
	oxygenLines, co2Lines := report, report
	for i := range report[0] {
		if hasLessOrEqualZerosThanOnes(i, oxygenLines) {
			oxygenLines = keepOnly(i, '1', oxygenLines)
		} else {
			oxygenLines = keepOnly(i, '0', oxygenLines)
		}
		if hasLessOrEqualZerosThanOnes(i, co2Lines) {
			co2Lines = keepOnly(i, '0', co2Lines)
		} else {
			co2Lines = keepOnly(i, '1', co2Lines)
		}
	}

	return bitStringToInt(oxygenLines[0]) * bitStringToInt(co2Lines[0])
}

func keepOnly(i int, c byte, lines []string) []string {
	if len(lines) == 1 {
		return lines
	}
	var result []string
	for _, line := range lines {
		if line[i] == c {
			result = append(result, line)
		}
	}
	return result
}

func bitStringToInt(s string) int {
	powOfTwo := 1 << (len(s) - 1)
	var result int
	for _, c := range s {
		if c == '1' {
			result += powOfTwo
		}
		powOfTwo >>= 1
	}
	return result
}

func main() {
	report := common.GetInputLines()
	fmt.Println(solve_03_1(report))
	fmt.Println(solve_03_2(report))
}
