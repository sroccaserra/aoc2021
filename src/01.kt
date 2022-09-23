import java.io.File
import aoc.common.getParsedLines

const val HUGE = 9999

fun solve1(numbers: List<Int>): Int {
    var result = 0
    var previous = HUGE
    for (n in numbers) {
        if (n > previous) {
            ++result
        }
        previous = n
    }

    return result
}

fun solve2(numbers: List<Int>): Int {
    var result = 0
    var p1 = HUGE
    var p2 = HUGE
    var p3 = HUGE
    for (n in numbers) {
        if (n + p1 + p2 > p1 + p2 + p3) {
            ++result
        }
        p3 = p2
        p2 = p1
        p1 = n
    }

    return result
}

fun main(args: Array<String>) {
    val numbers = getParsedLines(args[0], String::toInt)
    println(solve1(numbers))
    println(solve2(numbers))
}
