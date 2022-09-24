require './src/common/common.rb'

HUGE = 9999

def solve_1(numbers)
  result = 0
  previous = HUGE
  numbers.each do |n|
    if n > previous then
      result += 1
    end
    previous = n
  end
  result
end

def solve_2(numbers)
  result = 0
  p1 = p2 = p3 = HUGE
  numbers.each do |n|
    if n + p1 + p2 > p1 + p2 + p3 then
      result += 1
    end
    p3, p2, p1 = p2, p1, n
  end
  result
end

if __FILE__ == $0
  numbers = get_parsed_lines(lambda { |line| line.to_i })
  puts solve_1(numbers)
  puts solve_2(numbers)
end
