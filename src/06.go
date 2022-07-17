package main

import (
	"fmt"

	. "aoc2021/src/common"
)

func solve_06(fishStates []int, nbDays int) int {
	var counters stateCounters
	for _, fishState := range fishStates {
		counters[fishState]++
	}
	for i := 0; i < nbDays; i++ {
		counters = counters.forNextDay()
	}
	return counters.sumFishes()
}

type stateCounters [9]int

func (self stateCounters) forNextDay() stateCounters {
	var result stateCounters
	nbBreeders := self[0]
	for i := 0; i < 8; i++ {
		result[i] = self[i+1]
	}
	result[6] += nbBreeders
	result[8] = nbBreeders
	return result
}

func (self stateCounters) sumFishes() int {
	var s int
	for _, count := range self {
		s += count
	}
	return s
}

func main() {
	fishStates := SplitToInts(",", GetInputLine())
	fmt.Println(solve_06(fishStates, 80))
	fmt.Println(solve_06(fishStates, 256))
}
