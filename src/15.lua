require 'src/common'
local heap = require 'src/heap'

function solve(grid, scale)
  local w = #grid[1]
  local h = #grid
  return lowest_risk_ucs(grid, w, h, scale, {1, 1})
end

function lowest_risk_ucs(grid, w, h, scale, src)
  local w_s, h_s = w*scale, h*scale
  local risks = {}
  setxy(risks, src, 0)
  local q = {encode(0, src)}
  while #q > 0 do
    local risk, p = decode(heap.pop(q))
    for n in all(neighbors(w_s, h_s, p)) do
      local new_risk = risk + compute_risk(grid, w, h, scale, n)
      local previous = getxy(risks, n)
      if nil == previous or new_risk < previous then
        setxy(risks, n, new_risk)
        heap.push(q, encode(new_risk, n))
      end
    end
  end
  return getxy(risks, {w_s, h_s})
end

function neighbors(w_s, h_s, p)
  local x, y = p[1], p[2]
  local result = {}
  for n in all({{x-1, y}, {x+1, y}, {x, y-1}, {x, y+1}}) do
    local xn, yn = n[1], n[2]
    if 1 <= xn and xn <= w_s and 1 <= yn and yn <= h_s then
      table.insert(result, n)
    end
  end
  return result
end

function compute_risk(grid, w, h, scale, p)
  local x, y = p[1], p[2]
  assert(1 <= x and x <= w*scale and 1 <= y and y <= h*scale, string.format("out: %d %d",x , y))
  local bonus = math.floor((x-1)/w) + math.floor((y-1)/h)
  local res = grid[(y-1)%h+1][(x-1)%w+1] + bonus
  return (res - 1)%9 + 1
end

function key(p)
  return string.format("%d,%d", p[1], p[2])
end

function encode(d, p)
  return string.format("%09d %s", d, key(p))
end

function decode(s)
  local it = string.gmatch(s, "%d+")
  return tonumber(it()), {tonumber(it()), tonumber(it())}
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
