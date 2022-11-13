load 'src/common/common.ijs'

solve =. verb define
'hpos depth1 depth2 aim' =. 0 0 0 0
for_command. y do.
    'direction value' =. command
    select. direction
    case. 'forward' do.
        hpos =. hpos + value
        depth2 =. depth2 + aim * value
    case. 'up' do.
        depth1 =. depth1 - value
        aim =. aim - value
    case. 'down' do.
        depth1 =. depth1 + value
        aim =. aim + value
    end.
end.
(hpos * depth1) , (hpos * depth2)
)

parse =. ({. , ".&.>@:}.) & ;:

commands =. > parse each getinputlines ''
'result1 result2' =. solve commands
echo result1
echo result2
