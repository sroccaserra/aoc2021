package main

import (
	"fmt"

	. "aoc2021/src/common"
)

func solve_07(burner func(int) int, positions []int) any {
	cheapest := 9999999999999
	for _, target := range positions {
		fuel := fuelForTarget(burner, target, positions)
		cheapest = Min(cheapest, fuel)
	}
	return cheapest
}

func fuelForTarget(burner func(int) int, target int, positions []int) int {
	var result int
	for _, v := range positions {
		distance := Abs(target - v)
		result += burner(distance)
	}
	return result
}

func fastBurner(n int) int {
	return (n * (n + 1)) / 2
}

func main() {
	numbers := SplitToInts(",", GetInputLine())
	fmt.Println(solve_07(Id[int], numbers))
	fmt.Println(solve_07(fastBurner, numbers))
}
