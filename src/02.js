import { getInputLines } from './common/common.js'

function solve_02(commands) {
  let hpos = 0, depth_1 = 0, depth_2 = 0, aim = 0
  for (const command of commands) {
    switch (command.direction) {
      case "forward":
        hpos += command.value
        depth_2 += aim * command.value
        break;
      case "up":
        depth_1 -= command.value
        aim -= command.value
        break;
      case "down":
        depth_1 += command.value
        aim += command.value
        break;
    }
  }
  return [hpos * depth_1, hpos * depth_2]
}

function parse(line) {
  const parts = line.split(' ')
  return {direction: parts[0], value: Number(parts[1])}
}

const commands = getInputLines().map(parse)
const [result_1, result_2] = solve_02(commands)
console.log(result_1)
console.log(result_2)
