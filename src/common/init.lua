function all(t)
  local i = 0
  return function() i = i + 1; return t[i] end
end

function map(f, t)
  local result = {}
  for _, v in ipairs(t) do
    table.insert(result, f(v))
  end
  return result
end

function setxy(m, x, y, v)
  if m[y] == nil then
    m[y] = {}
  end
  m[y][x] = v
end

function getxy(m, x, y)
  if m[y] == nil then
    return nil
  end
  return m[y][x]
end

function dump(o)
  if type(o) == 'table' then
    local s = '{ '
    for k,v in pairs(o) do
      if type(k) ~= 'number' then k = '"'..k..'"' end
      s = s .. '['..k..'] = ' .. dump(v) .. ','
    end
    return s .. '} '
  else
    return tostring(o)
  end
end

---
-- IO


function getParsedLines(parse_fn)
  local result = {}
  for line in io.lines(arg[1]) do
    table.insert(result, parse_fn(line))
  end
  return result
end

function readlines(options)
  options = options or 'l'
  local result = {}
  for line in io.input(arg[1]):lines(options) do
    table.insert(result, line)
  end
  return result
end
