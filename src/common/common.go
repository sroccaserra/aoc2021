package common

import (
	"bufio"
	"io"
	"os"
	"strconv"
	"strings"
)

func GetInputLines() []string {
	return GetParsedLines(id[string])
}

func GetInputInts() []int {
	return GetParsedLines(parseInt)
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
		result = append(result, parseInt(cs))
	}
	return result
}

func id[T any](x T) T {
	return x
}

func parseInt(s string) int {
	n, _ := strconv.Atoi(s)
	return n
}
