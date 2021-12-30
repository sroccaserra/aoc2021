function all(t)
  local i = 0
  return function() i = i + 1; return t[i] end
end

function map(f, t)
  local result = {}
  for i, v in ipairs(t) do
    result[i] = f(v)
  end
  return result
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

function readlines()
  local result = {}
  while true do
    local line = io.read("*line")
    if not line then
      break
    end
    table.insert(result, line)
  end
  return result
end
