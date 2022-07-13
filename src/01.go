package main

import (
    "bufio"
    "fmt"
    "math"
    "os"
    "strconv"
)

func main() {
    // scanner := bufio.NewScanner(os.Stdin)
    // fmt.Println(os.Args)
    reader, _ := os.Open("src/01.in")
    scanner := bufio.NewScanner(reader)
    var numbers []int
    for scanner.Scan() {
        n, _ := strconv.Atoi(scanner.Text())
        numbers = append(numbers, n)
    }
    fmt.Println(solve(numbers))
}

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
