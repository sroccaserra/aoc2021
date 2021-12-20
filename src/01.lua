function solve(numbers)
  previous = 99999
  result = 0
  for _, n in ipairs(numbers) do
    if n > previous then
      result = result + 1
    end
    previous = n
  end
  return result
end

function parse()
  numbers = {}
  while true do
    line = io.read("*line")
    if not line then
      break
    end
    n = tonumber(line)
    table.insert(numbers, n)
  end
  return numbers
end

numbers = parse()
print(solve(numbers))
