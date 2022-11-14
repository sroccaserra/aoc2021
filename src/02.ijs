load 'src/common/common.ijs'

solve =. monad : '0 0 0 0 results F.. applycommand y'

applycommand =: dyad define
'hpos depth1 depth2 aim' =. y
'direction value' =. x
select. direction
case. 'forward' do. (hpos + value) 0 } (depth2 + aim * value) 2 } y
case. 'up'      do. (aim - value) 3 } (depth1 - value) 1 } y
case. 'down'    do. (aim + value) 3 } (depth1 + value) 1 } y
end.
)

results =: (0&{ * 1&{) , (0&{ * 2&{)

parse =. ({. , [: ".&.> }.) & ;:
commands =. > parse each getinputlines ''
echo 2 1 $ solve commands
