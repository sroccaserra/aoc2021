require 'src.common.common'

local actions = {
  forward = function(submarine, value)
    submarine.hpos = submarine.hpos + value
    submarine.depth_2 = submarine.depth_2 + submarine.aim * value
  end,
  up = function(submarine, value)
    submarine.depth_1 = submarine.depth_1 - value
    submarine.aim = submarine.aim - value
  end,
  down = function(submarine, value)
    submarine.depth_1 = submarine.depth_1 + value
    submarine.aim = submarine.aim + value
  end,
}

function solve(commands)
  local submarine = {hpos = 0, depth_1 = 0, depth_2 = 0, aim = 0}
  for command in all(commands) do
    actions[command.direction](submarine, command.value)
  end
  return submarine.hpos * submarine.depth_1, submarine.hpos * submarine.depth_2
end

function parse(line)
  local match_it = line:gmatch('(%w+) (%w+)')
  local d, v = match_it()
  return {direction = d, value = tonumber(v)}
end

local commands = getParsedLines(parse)
local result_1, result_2 = solve(commands)
print(result_1)
print(result_2)
