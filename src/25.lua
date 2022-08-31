require 'src.common.common'

function solve(floor)
  local w = #floor[1]
  local h = #floor
  local easts = {}
  local souths = {}
  for y=1,h do
    row = floor[y]
    for x=1,w do
      c = row:sub(x,x)
      if c == '>' then
        set(easts, x, y)
      elseif c == 'v' then
        set(souths, x, y)
      end
    end
  end

  local n = 0
  while true do
    n = n + 1
    easts, souths, moved = step(w, h, easts, souths)
    if not moved then
      break
    end
  end
  print(n)
end

function step(w, h, easts, souths)
  local moved = false
  local new_easts = {}
  for y in pairs(easts) do
    for x in pairs(easts[y]) do
      dest_x = east_of(w, x)
      if is_occupied(easts, souths, dest_x, y) then
        set(new_easts, x, y)
      else
        moved = true
        set(new_easts, dest_x, y)
      end
    end
  end

  local new_souths = {}
  for y in pairs(souths) do
    for x in pairs(souths[y]) do
      dest_y = south_of(h, y)
      if is_occupied(new_easts, souths, x, dest_y) then
        set(new_souths, x, y)
      else
        moved = true
        set(new_souths, x, dest_y)
      end
    end
  end
  return new_easts, new_souths, moved
end

function display(w, h, easts, souths)
  for y=1,h do
    local row = ''
    for x=1,w do
      local c
      if get(easts, x, y) then
        c = '>'
      elseif get(souths, x, y) then
        c = 'v'
      else
        c = '.'
      end
      row = row..c
    end
    print(row)
  end
end

function is_occupied(easts, souths, x, y)
  return get(easts, x, y) or get(souths, x, y)
end

function east_of(w, x)
  if x == w then return 1 else return x + 1 end
end

function south_of(h, y)
  if y == h then return 1 else return y + 1 end
end

function set(t, x, y)
  if not t[y] then
    t[y] = {}
  end
  t[y][x] = true
end

function get(t, x, y)
  return t[y] and t[y][x]
end

floor = readlines()
print(solve(floor))
