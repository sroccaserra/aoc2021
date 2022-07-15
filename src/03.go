package main

import (
	"fmt"

	"aoc2021/src/common"
)

func solve_03_1(report []string) int {
	nbBits := len(report[0])
	powOfTwo := 1 << (nbBits - 1)
	var gamma, epsilon int
	for i := 0; i < nbBits; i++ {
		if hasMoreOnes(i, report) {
			gamma += powOfTwo
		} else {
			epsilon += powOfTwo
		}
		powOfTwo >>= 1
	}
	return gamma * epsilon
}

func hasMoreOnes(i int, report []string) bool {
	var nbOnes, nbZeros int
	for _, line := range report {
		if line[i] == '0' {
			nbZeros++
		} else {
			nbOnes++
		}
	}
	return nbOnes > nbZeros
}

func main() {
	report := common.GetInputLines()
	fmt.Println(solve_03_1(report))
}
