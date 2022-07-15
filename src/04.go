package main

import (
	"fmt"
	"strconv"
	"strings"

	"aoc2021/src/common"
)

func solve_04_1(order order, grids []grid) int {
	for _, n := range order {
		for _, grid := range grids {
			mark(n, grid)
			if hasWon(grid) {
				return n * sumUnmarked(grid)
			}
		}
	}
	return -1
}

func mark(n int, grid grid) {
	for _, row := range grid {
		for j, val := range row {
			if val == n {
				row[j] = marked
			}
		}
	}
}

const marked = -1

func isMarked(n int) bool {
	return n == marked
}

func hasWon(grid grid) bool {
	for _, row := range grid {
		if all(isMarked, row) {
			return true
		}
	}
	for j := range grid[0] {
		allMarked := true
		for _, row := range grid {
			if !isMarked(row[j]) {
				allMarked = false
			}
		}
		if allMarked {
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

func solve_04_2(order order, grids []grid) int {
	var lastN int
	var lastGrid grid
	winningGrids := map[int]bool{}
	for _, n := range order {
		for k, grid := range grids {
			if winningGrids[k] {
				continue
			}
			mark(n, grid)
			if hasWon(grid) {
				lastN = n
				lastGrid = grid
				winningGrids[k] = true
			}
		}
	}
	return lastN * sumUnmarked(lastGrid)
}

type grid [][]int
type order []int

func copyGrids(grids []grid) []grid {
	result := make([]grid, len(grids))
	for k, srcGrid := range grids {
		result[k] = make(grid, len(srcGrid))
		dstGrid := result[k]
		for i, row := range srcGrid {
			dstGrid[i] = make([]int, len(row))
			copy(dstGrid[i], srcGrid[i])
		}
	}
	return result
}

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
	fmt.Println(solve_04_1(order, copyGrids(grids)))
	fmt.Println(solve_04_2(order, copyGrids(grids)))
}
