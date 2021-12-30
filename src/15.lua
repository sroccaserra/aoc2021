require 'src/common'
local heap = require 'src/heap'

function solve(grid, scale)
  local w = #grid[1]
  local h = #grid
  return lowest_risk_ucs(grid, w, h, scale)
end

function lowest_risk_ucs(grid, w, h, scale)
  local w_s, h_s = w*scale, h*scale
  local x0, y0 = 1, 1

  local risks = {}
  setxy(risks, x0, y0, 0)
  local pq = {encode(0, x0, y0)}
  while #pq > 0 do
    local risk, x, y = decode(heap.pop(pq))
    for n in all(neighbors(w_s, h_s, x, y)) do
      local xn, yn = n[1], n[2]
      local new_risk = risk + compute_risk(grid, w, h, scale, xn, yn)
      local old_risk = getxy(risks, xn, yn)
      if nil == old_risk or new_risk < old_risk then
        setxy(risks, xn, yn, new_risk)
        heap.push(pq, encode(new_risk, xn, yn))
      end
    end
  end

  return getxy(risks, w_s, h_s)
end

function neighbors(w_s, h_s, x, y)
  local result = {}
  for n in all({{x-1, y}, {x+1, y}, {x, y-1}, {x, y+1}}) do
    local xn, yn = n[1], n[2]
    if 1 <= xn and xn <= w_s and 1 <= yn and yn <= h_s then
      table.insert(result, n)
    end
  end
  return result
end

function compute_risk(grid, w, h, scale, x, y)
  assert(1 <= x and x <= w*scale and 1 <= y and y <= h*scale, string.format("out: %d %d",x , y))
  local bonus = math.floor((x-1)/w) + math.floor((y-1)/h)
  local res = grid[(y-1)%h+1][(x-1)%w+1] + bonus
  return (res - 1)%9 + 1
end

function encode(d, x, y)
  return string.format("%09d %d,%d", d, x, y)
end

function decode(s)
  local it = string.gmatch(s, "%d+")
  return tonumber(it()), tonumber(it()), tonumber(it())
end

lines = readlines()
grid = {}
for line in all(lines) do
  local ns = {}
  table.insert(grid, ns)
  for i=1,#line do
    table.insert(ns, tonumber(string.sub(line, i, i)))
  end
end

print(solve(grid, 1))
print(solve(grid, 5))
