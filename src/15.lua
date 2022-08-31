require 'src.common.common'
heap = require 'src.common.heap'

local insert = heap.insert
local remove_min = heap.remove_min

function solve(grid, scale)
  local w = #grid[1]
  local h = #grid
  return lowest_risk_ucs(grid, w, h, scale)
end

-- Note: version inspired by:
-- * https://stanford-cs221.github.io/autumn2019/live/search1/
-- Note: lookup past versions of this file to see alternative implementations
function lowest_risk_ucs(grid, w, h, scale)
  local w_s, h_s = w*scale, h*scale
  local x0, y0 = 1, 1

  local frontier = create_pq()
  update_pq(frontier, x0, y0, 0)
  while true do
    x, y, past_cost = remove_min_pq(frontier)
    if x == w_s and y == h_s then
      return past_cost
    end
    for n in all(neighbors(w_s, h_s, x, y)) do
      local xn, yn = table.unpack(n)
      local cost = compute_risk(grid, w, h, scale, xn, yn)
      update_pq(frontier, xn, yn, past_cost + cost)
    end
  end
  error('Error: not found')
end

function create_pq()
  return {
    heap = heap.create(),
    priorities = {},
    DONE = -100000
  }
end

function update_pq(pq, x, y, new_priority)
  local old_priority = getxy(pq.priorities, x, y)
  if nil == old_priority or new_priority < old_priority then
    setxy(pq.priorities, x, y, new_priority)
    insert(pq.heap, node(x, y, new_priority))
    return true
  end
  return false
end

function remove_min_pq(pq)
  while #pq.heap > 0 do
    local x, y, priority = table.unpack(remove_min(pq.heap))
    if getxy(pq.priorities, x, y) ~= pq.DONE then
      setxy(pq.priorities, x, y, pq.DONE)
      return x, y, priority
    end
  end
  error('Error: trying to pop an empty priority queue.')
end

local COST = 3
local node_mt = {__lt = function(a, b) return a[COST] < b[COST] end}

function node(x, y, cost)
  local result = {x, y, cost}
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
