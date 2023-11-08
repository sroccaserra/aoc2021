load 'src/common/common.ijs'

forward =: {{ y,0 }}
up =: {{ 0,-y }}
down =: {{ 0,y }}

acc =: 4 : 0
    f =. {.>x
    aim =. 1&{ >y
    ((>x),f*aim) + >y
)

solve =: 3 : 0
    values =. acc/ |. (<0 0 0) , y

    h =. 0&{values
    depth1 =. 1&{values
    depth2 =. 2&{values

    (h*depth1),(h*depth2)
)

commands =. ". each getinputlines ''
echo 2 1 $ solve commands

NB. Tests
{{
    testLines =: (<'forward 5'),(<'down 5'),(<'forward 8'),(<'up 3'),(<'down 8'),(<'forward 2')
    testCommands =: ". each testLines
    assert. 15 10 60 -: acc/ |. (<0 0 0) , testCommands
    assert. 150 900 -: solve testCommands
}}''
