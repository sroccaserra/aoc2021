require 'src.common.common'

local huge = math.huge

function solve_1(numbers)
  local previous = huge
  local result = 0
  for n in all(numbers) do
    if n > previous then
      result = result + 1
    end
    previous = n
  end
  return result
end

function solve_2(numbers)
  local p1, p2, p3 = huge, huge, huge
  local result = 0
  for n in all(numbers) do
    if n + p1 + p2 > p1 + p2 + p3 then
      result = result + 1
    end
    p1, p2, p3 = n, p1, p2
  end
  return result
end

numbers = readlines('n')

print(solve_1(numbers))
print(solve_2(numbers))
