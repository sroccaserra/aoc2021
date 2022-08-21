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

func solve_09_2(floorMap floorMap) any {
	var basinSizes []int
	for _, point := range floorMap.findLowPoints() {
		basinSizes = append(basinSizes, floorMap.basinSizeAt(point))
	}
	sort.Sort(sort.Reverse(sort.IntSlice(basinSizes)))
	return basinSizes[0] * basinSizes[1] * basinSizes[2]
}

type floorMap struct {
	lines []string
	w, h  int
}

func (self *floorMap) findLowPoints() []floorPoint {
	var result []floorPoint
	for i := 0; i < self.h; i++ {
		for j := 0; j < self.w; j++ {
			point := floorPoint{i, j}
			if self.isLowPoint(point) {
				result = append(result, point)
			}
		}
	}
	return result
}

func (self *floorMap) isLowPoint(point floorPoint) bool {
	c := self.charAt(point)
	for _, n := range self.neighbors(point) {
		if self.charAt(n) <= c {
			return false
		}
	}
	return true
}

func (self *floorMap) riskAt(point floorPoint) int {
	return ParseDigit(self.charAt(point)) + 1
}

func (self *floorMap) basinSizeAt(lowPoint floorPoint) int {
	result := 0
	known := map[floorPoint]bool{}
	var q []floorPoint

	process := func(point floorPoint) {
		result += 1
		Enqueue(&q, point)
		known[point] = true
	}

	process(lowPoint)
	for len(q) > 0 {
		point := Dequeue(&q)
		for _, n := range self.flowingNeighbors(point) {
			if !known[n] {
				process(n)
			}
		}
	}
	return result
}

func (self *floorMap) flowingNeighbors(point floorPoint) []floorPoint {
	c := self.charAt(point)

	var result []floorPoint
	for _, n := range self.neighbors(point) {
		neighborChar := self.charAt(n)
		if c < neighborChar && '9' != neighborChar {
			result = append(result, n)
		}
	}
	return result
}

func (self *floorMap) neighbors(point floorPoint) []floorPoint {
	var result []floorPoint
	if 0 < point.i {
		result = append(result, floorPoint{point.i - 1, point.j})
	}
	if point.i < self.h-1 {
		result = append(result, floorPoint{point.i + 1, point.j})
	}
	if 0 < point.j {
		result = append(result, floorPoint{point.i, point.j - 1})
	}
	if point.j < self.w-1 {
		result = append(result, floorPoint{point.i, point.j + 1})
	}
	return result
}

func (self *floorMap) charAt(point floorPoint) byte {
	return self.lines[point.i][point.j]
}

type floorPoint struct {
	i, j int
}

func main() {
	lines := GetInputLines()
	floorMap := floorMap{lines, len(lines[0]), len(lines)}
	fmt.Println(solve_09_1(floorMap))
	fmt.Println(solve_09_2(floorMap))
}
