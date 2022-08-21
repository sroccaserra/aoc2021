package main

import (
	"fmt"

	. "aoc2021/src/common"
)

func solve_09_1(floorMap floorMap) any {
	return floorMap.sumLowPointRisks()
}

type floorMap struct {
	lines []string
	w, h  int
}

func (self *floorMap) sumLowPointRisks() int {
	result := 0
	for i := 0; i < self.w; i++ {
		line := self.lines[i]
		for j := 0; j < self.w; j++ {
			if self.isLowPoint(i, j) {
				result += ParseDigit(line[j]) + 1
			}
		}
	}
	return result
}

func (self *floorMap) isLowPoint(i, j int) bool {
	c := self.charAt(i, j)
	if 0 < i && self.charAt(i-1, j) <= c {
		return false
	}
	if i < self.w-1 && self.charAt(i+1, j) <= c {
		return false
	}
	if 0 < j && self.charAt(i, j-1) <= c {
		return false
	}
	if j < self.h-1 && self.charAt(i, j+1) <= c {
		return false
	}
	return true
}

func (self *floorMap) charAt(i, j int) byte {
	return self.lines[i][j]
}

func main() {
	lines := GetInputLines()
	floorMap := floorMap{lines, len(lines[0]), len(lines)}
	fmt.Println(solve_09_1(floorMap))
}
