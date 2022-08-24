package main

import (
	"fmt"

	"aoc2021/src/common"
)

const huge = 9999999999

func solve_01_1(numbers []int) int {
	previous := huge
	result := 0
	for _, n := range numbers {
		if n > previous {
			result++
		}
		previous = n
	}
	return result
}

func solve_01_2(numbers []int) int {
	var p1, p2, p3 = huge, huge, huge
	result := 0
	for _, n := range numbers {
		if n+p1+p2 > p1+p2+p3 {
			result++
		}
		p1, p2, p3 = n, p1, p2
	}
	return result
}

func main() {
	numbers := common.GetInputInts()
	fmt.Println(solve_01_1(numbers))
	fmt.Println(solve_01_2(numbers))
}
