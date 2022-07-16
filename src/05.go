package main

import (
	"fmt"
	"strings"
	"unicode"

	. "aoc2021/src/common"
)

func solve_05_1(lines []line) int {
	grid := map[string]int{}
	for _, line := range lines {
		if line.x1 == line.x2 || line.y1 == line.y2 {
			markStraightLine(line, grid)
		}
	}
	return countResult(grid)
}

func solve_05_2(lines []line) int {
	grid := map[string]int{}
	for _, line := range lines {
		if line.x1 == line.x2 || line.y1 == line.y2 {
			markStraightLine(line, grid)
		} else {
			markDiagonalLine(line, grid)
		}
	}
	return countResult(grid)
}

func markStraightLine(line line, grid map[string]int) {
	minX, maxX := Min(line.x1, line.x2), Max(line.x1, line.x2)
	minY, maxY := Min(line.y1, line.y2), Max(line.y1, line.y2)
	for y := minY; y <= maxY; y++ {
		for x := minX; x <= maxX; x++ {
			key := makeKey(x, y)
			grid[key] += 1
		}
	}
}

func markDiagonalLine(line line, grid map[string]int) {
	minX, maxX := Min(line.x1, line.x2), Max(line.x1, line.x2)
	width := maxX - minX
	dx := (line.x2 - line.x1) / width
	dy := (line.y2 - line.y1) / width
	for x, y := line.x1, line.y1; x != line.x2+dx || y != line.y2+dy; x, y = x+dx, y+dy {
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
	parts := strings.FieldsFunc(s, func(c rune) bool { return !unicode.IsNumber(c) })
	var numbers []int
	for _, part := range parts {
		numbers = append(numbers, ParseInt(part))
	}
	return line{numbers[0], numbers[1], numbers[2], numbers[3]}
}

func main() {
	lines := GetParsedLines(parse_05)
	fmt.Println(solve_05_1(lines))
	fmt.Println(solve_05_2(lines))
}
