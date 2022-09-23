package aoc.common

import java.io.File

public fun <T> getParsedLines(filename: String, parse: (String) -> T): List<T> {
    return File(filename)
        .readLines()
        .map(parse)
}
