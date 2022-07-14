package main

import (
    "fmt"
    "math"
    "strconv"
    "aoc2021/src/common"
)

func solve(numbers []int) int {
    previous := math.MaxInt
    result := 0
    for _, n := range numbers {
        if n > previous {
            result += 1
        }
        previous = n
    }
    return result
}

func main() {
    lines := common.GetInputLines()
    var numbers []int
    for _, line := range lines {
        n, _ := strconv.Atoi(line)
        numbers = append(numbers, n)
    }
    fmt.Println(solve(numbers))
}
