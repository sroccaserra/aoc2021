local M = {}

---
-- Simple heap, from the Algorithm Design Manual, 4.3.1, p. 109

local NONE = -1
local floor = math.floor

local function _parent(n)
  if n == 1 then
    return NONE
  end
  return floor(n/2)
end

local function _young_child(n)
  return 2*n
end

local function _bubble_up(h, p)
  local parent = _parent(p)

  if parent == NONE then
    return
  end

  if h[parent] > h[p] then
    h[p], h[parent] = h[parent], h[p]
    _bubble_up(h, parent)
  end
end

local function _bubble_down(h, p)
  local c = _young_child(p)
  local min_index = p

  for i=0,1 do
    if c+i <= #h then
      if h[min_index] > h[c+i] then
        min_index = c+i
      end
    end
  end

  if min_index ~= p then
    h[p], h[min_index] = h[min_index], h[p]
    _bubble_down(h, min_index)
  end
end

---
-- Public interface

function M.create(ns)
  ns = ns or {}
  local result = {}

  for _,n in ipairs(ns) do
    M.insert(result, n)
  end

  return result
end

function M.insert(h, x)
  table.insert(h, x)
  _bubble_up(h, #h)
end

function M.remove_min(h)
  local n = #h

  if n == 0 then
    error('Error: trying to pop from empty heap.')
  end

  local result = h[1]
  h[1] = h[n]
  table.remove(h)
  _bubble_down(h, 1)

  return result
end

return M
