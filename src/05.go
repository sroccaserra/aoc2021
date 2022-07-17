package main

import (
	"fmt"

	. "aoc2021/src/common"
)

func solve_05_1(lines []line) int {
	grid := map[point]int{}
	for _, line := range lines {
		if line.x1 == line.x2 || line.y1 == line.y2 {
			markLine(line, grid)
		}
	}
	return countResult(grid)
}

func solve_05_2(lines []line) int {
	grid := map[point]int{}
	for _, line := range lines {
		markLine(line, grid)
	}
	return countResult(grid)
}

func markLine(line line, grid map[point]int) {
	deltaX, deltaY := line.x2-line.x1, line.y2-line.y1
	dx, dy := direction(deltaX), direction(deltaY)
	n := Max(Abs(deltaX), Abs(deltaY))
	for x, y, i := line.x1, line.y1, 0; i <= n; x, y, i = x+dx, y+dy, i+1 {
		grid[point{x, y}]++
	}
}

func direction(delta int) int {
	switch {
	case delta < 0:
		return -1
	case delta > 0:
		return 1
	default:
		return 0
	}
}

func countResult(grid map[point]int) int {
	var result int
	for _, v := range grid {
		if v > 1 {
			result++
		}
	}
	return result
}

type line struct{ x1, y1, x2, y2 int }
type point struct{ x, y int }

func parse_05(s string) line {
	var x1, y1, x2, y2 int
	fmt.Sscanf(s, "%d,%d -> %d,%d", &x1, &y1, &x2, &y2)
	return line{x1, y1, x2, y2}
}

func main() {
	lines := GetParsedLines(parse_05)
	fmt.Println(solve_05_1(lines))
	fmt.Println(solve_05_2(lines))
}
