require './src/common/common.rb'

HUGE = 9999

def solve(commands)
  hpos = depth_1 = depth_2 = aim = 0
  commands.each do |command|
    case command.direction
    when 'forward'
      hpos += command.value
      depth_2 += aim * command.value
    when 'up'
      depth_1 -= command.value
      aim -= command.value
    when 'down'
      depth_1 += command.value
      aim += command.value
    end
  end
  return hpos * depth_1, hpos * depth_2
end

Command = Struct.new(:direction, :value)

parse = lambda do |line|
  parts = line.split
  Command.new(parts[0], parts[1].to_i)
end

if __FILE__ == $0
  commands = get_parsed_lines(parse)
  result_1, result_2 = solve(commands)
  puts result_1
  puts result_2
end
