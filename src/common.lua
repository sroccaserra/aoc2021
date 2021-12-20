function all(t)
  local i = 0
  return function() i = i + 1; return t[i] end
end

function map(f, t)
  result = {}
  for i, v in ipairs(t) do
    result[i] = f(v)
  end
  return result
end

function readlines()
  result = {}
  while true do
    line = io.read("*line")
    if not line then
      break
    end
    table.insert(result, line)
  end
  return result
end
