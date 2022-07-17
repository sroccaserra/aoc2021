package common

import (
	"bufio"
	"io"
	"os"
	"strconv"
	"strings"
)

func GetInputLines() []string {
	return GetParsedLines(Id[string])
}

func GetInputLine() string {
	return GetParsedLines(Id[string])[0]
}

func GetInputInts() []int {
	return GetParsedLines(ParseInt)
}

func GetParsedLines[T any](parse func(string) T) []T {
	var result []T
	var reader io.Reader
	if len(os.Args) > 1 {
		filename := os.Args[1]
		reader, _ = os.Open(filename)
	} else {
		reader = os.Stdin
	}
	scanner := bufio.NewScanner(reader)
	for scanner.Scan() {
		result = append(result, parse(scanner.Text()))
	}
	return result
}
func SplitToInts(sep string, s string) []int {
	var result []int
	for _, cs := range strings.Split(s, sep) {
		result = append(result, ParseInt(cs))
	}
	return result
}

func Id[T any](x T) T {
	return x
}

func ParseInt(s string) int {
	n, _ := strconv.Atoi(s)
	return n
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func Abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}
