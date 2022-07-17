package main

import (
	"fmt"

	. "aoc2021/src/common"
)

func solve_05_1(lines []line) int {
	grid := map[string]int{}
	for _, line := range lines {
		if line.x1 == line.x2 || line.y1 == line.y2 {
			markLine(line, grid)
		}
	}
	return countResult(grid)
}

func solve_05_2(lines []line) int {
	grid := map[string]int{}
	for _, line := range lines {
		markLine(line, grid)
	}
	return countResult(grid)
}

func markLine(line line, grid map[string]int) {
	deltaX, deltaY := line.x2-line.x1, line.y2-line.y1
	var dx, dy int
	switch {
	case deltaX < 0:
		dx = -1
	case deltaX > 0:
		dx = 1
	default:
		dx = 0
	}
	switch {
	case deltaY < 0:
		dy = -1
	case deltaY > 0:
		dy = 1
	default:
		dy = 0
	}
	n := Max(Abs(deltaX), Abs(deltaY))
	for x, y, i := line.x1, line.y1, 0; i <= n; x, y, i = x+dx, y+dy, i+1 {
		key := makeKey(x, y)
		grid[key] += 1
	}
}

func countResult(grid map[string]int) int {
	var result int
	for _, v := range grid {
		if v > 1 {
			result += 1
		}
	}
	return result
}

type line struct{ x1, y1, x2, y2 int }

func makeKey(x int, y int) string {
	return fmt.Sprintf("%d,%d", x, y)
}

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
