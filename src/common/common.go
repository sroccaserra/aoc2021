package common

import (
    "bufio"
    "io"
    "os"
)

func GetInputLines() []string {
    var result []string
    var reader io.Reader
    if len(os.Args) > 1 {
        filename := os.Args[1]
        reader, _ = os.Open(filename)
    } else {
        reader = os.Stdin
    }
    scanner := bufio.NewScanner(reader)
    for scanner.Scan() {
        result = append(result, scanner.Text())
    }
    return result
}
