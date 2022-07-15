package main

import (
	"fmt"
	"strconv"
	"strings"

	"aoc2021/src/common"
)

func solve_04_1(order order, grids []grid) int {
	var lastN int
	var winningGrid grid
out:
	for _, n := range order {
		for _, grid := range grids {
			mark(n, grid)
			if hasWon(grid) {
				lastN = n
				winningGrid = grid
				break out
			}
		}
	}
	return lastN * sumUnmarked(winningGrid)
}

func mark(n int, grid grid) {
	for _, row := range grid {
		for j, val := range row {
			if val == n {
				row[j] = marked(val)
			}
		}
	}
}

func reset(grid grid) {
	for _, row := range grid {
		for j, val := range row {
			if isMarked(val) {
				row[j] = marked(val)
			}
		}
	}
}

func marked(n int) int {
	return -(n + 1)
}

func isMarked(n int) bool {
	return n < 0
}

func hasWon(grid grid) bool {
	for _, row := range grid {
		if all(isMarked, row) {
			return true
		}
	}
	for j := 0; j < len(grid[0]); j++ {
		var col []int
		for _, row := range grid {
			col = append(col, row[j])
		}
		if all(isMarked, col) {
			return true
		}
	}
	return false
}

func sumUnmarked(grid grid) int {
	var result int
	for _, row := range grid {
		for _, val := range row {
			if !isMarked(val) {
				result += val
			}
		}
	}
	return result
}

func all[T any](pred func(T) bool, values []T) bool {
	for _, x := range values {
		if !pred(x) {
			return false
		}
	}
	return true
}

type grid [][]int
type order []int

func parse_04(lines []string) (order, []grid) {
	order := common.SplitToInts(",", lines[0])
	var grids []grid
	for i := 0; i < len(lines)-6; i += 6 {
		var grid grid
		for j := 0; j < 5; j++ {
			line := lines[i+j+2]
			fields := strings.Fields(line)
			var numbers []int
			for _, f := range fields {
				n, _ := strconv.Atoi(f)
				numbers = append(numbers, n)
			}
			grid = append(grid, numbers)
		}
		grids = append(grids, grid)
	}
	return order, grids
}

func main() {
	lines := common.GetInputLines()
	order, grids := parse_04(lines)
	fmt.Println(solve_04_1(order, grids))
}
