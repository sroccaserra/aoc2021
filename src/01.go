package main

import (
    "fmt"
    "math"
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
    numbers := common.GetInputInts()
    fmt.Println(solve(numbers))
}
