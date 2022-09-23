import aoc.common.getParsedLines

fun solve(commands: List<Command>): Pair<Int, Int> {
    var hpos = 0
    var depth_1 = 0
    var depth_2 = 0
    var aim = 0
    for (command in commands) {
        when (command.direction) {
            "forward" -> {
                hpos += command.value
                depth_2 += aim * command.value
            }
            "up" -> {
                depth_1 -= command.value
                aim -= command.value
            }
            "down" -> {
                depth_1 += command.value
                aim += command.value
            }
        }
    }
    return Pair(hpos * depth_1, hpos * depth_2)
}

data class Command(val direction: String, val value: Int)

fun parseCommand(line: String): Command {
    val parts = line.split(" ")
    return Command(parts[0], parts[1].toInt())
}

fun main(args: Array<String>) {
    val commands = getParsedLines<Command>(args[0], ::parseCommand)
    val (result1, result2) = solve(commands)
    println(result1)
    println(result2)
}
