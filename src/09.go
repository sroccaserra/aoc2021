package main

import (
	"fmt"
	"sort"

	. "aoc2021/src/common"
)

func solve_09_1(floorMap floorMap) int {
	result := 0
	for _, point := range floorMap.findLowPoints() {
		result += floorMap.riskAt(point)
	}
	return result
}

type floorMap struct {
	lines []string
	w, h  int
}

func (self *floorMap) findLowPoints() []floorPoint {
	var result []floorPoint
	for i := 0; i < self.w; i++ {
		for j := 0; j < self.w; j++ {
			if self.isLowPoint(i, j) {
				result = append(result, floorPoint{i, j})
			}
		}
	}
	return result
}

func (self *floorMap) riskAt(point floorPoint) int {
	return ParseDigit(self.charAt(point.i, point.j)) + 1
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

type floorPoint struct {
	i, j int
}

func main() {
	lines := GetInputLines()
	floorMap := floorMap{lines, len(lines[0]), len(lines)}
	fmt.Println(solve_09_1(floorMap))
}
