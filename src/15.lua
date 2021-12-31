require 'src/common'
heap = require 'src/heap'

local insert = heap.insert
local find = heap.find
local replace = heap.replace
local pop_min = heap.pop_min

function solve(grid, scale)
  local w = #grid[1]
  local h = #grid
  return lowest_risk_ucs(grid, w, h, scale)
end

function lowest_risk_ucs(grid, w, h, scale)
  local w_s, h_s = w*scale, h*scale
  local x0, y0 = 1, 1

  local pq = heap.create({node(0, x0, y0)})
  local closed = {}
  while #pq > 0 do
    local risk, x, y = table.unpack(pop_min(pq))
    if x == w_s and y == h_s then
      return risk
    end
    setxy(closed, x, y, true)
    for n in all(neighbors(w_s, h_s, x, y)) do
      local xn, yn = n[1], n[2]
      local new_risk = risk + compute_risk(grid, w, h, scale, xn, yn)
      local i, prev = find(pq, node(-1, xn, yn))
      if not getxy(closed, xn, yn) and nil == i then
        insert(pq, node(new_risk, xn, yn))
      elseif nil ~= i and prev[1] > new_risk then
        replace(pq, i, node(new_risk, xn, yn))
      end
    end
  end
end

local node_mt = {
  __lt = function(a, b) return a[1] < b[1] end,
  __eq = function(a, b) return a[2] == b[2] and a[3] == b[3] end
}

function node(cost, x, y)
  local result = {cost, x, y}
  setmetatable(result, node_mt)
  return result
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
