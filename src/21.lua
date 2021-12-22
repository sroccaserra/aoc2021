PLAYER_1_START = 8
PLAYER_2_START = 7
-- PLAYER_1_START = 4
-- PLAYER_2_START = 8

function solve_1(p1_start, p2_start)
  local roll_dice = create_dice()
  local p1_pos = p1_start
  local p1_score = 0
  local p2_pos = p2_start
  local p2_score = 0
  local nb_rolls = 0

  function roll_3_times()
    local result = 0
    for i=1,3 do
      nb_rolls = nb_rolls + 1
      result = result + roll_dice()
    end
    return result
  end

  while true do
    local rolls = roll_3_times()
    p1_pos = (p1_pos + rolls -1)%10 + 1
    p1_score = p1_score + p1_pos
    if p1_score >= 1000 then
      break
    end

    local rolls = roll_3_times()
    p2_pos = (p2_pos + rolls -1)%10 + 1
    p2_score = p2_score + p2_pos
    if p2_score >= 1000 then
      break
    end
  end

  return nb_rolls*math.min(p1_score, p2_score)
end

function create_dice()
  local n = 0
  return function()
      n = n + 1
      if n > 100 then
        n = n - 100
      end
      return n
  end
end

print(solve_1(PLAYER_1_START, PLAYER_2_START))
