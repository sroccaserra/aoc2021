Object subclass: Submarine [
    | hpos depth_1 depth_2 aim |
    Submarine class >> new [
        ^super new init ; yourself
    ]
    init [
        hpos := 0.
        depth_1 := 0.
        depth_2 := 0.
        aim := 0.
    ]
    execute: aCommand [
        | direction value selector |
        direction := aCommand at: #direction.
        value := aCommand at: #value.
        selector := (direction, ':') asSymbol.
        self perform: selector with: value.
    ]
    forward: value [
        hpos := hpos + value.
        depth_2 := depth_2 + (aim * value).
    ]
    up: value [
        depth_1 := depth_1 - value.
        aim := aim - value.
    ]
    down: value [
        depth_1 := depth_1 + value.
        aim := aim + value.
    ]
    hpos [
        ^hpos
    ]
    depth_1 [
        ^depth_1
    ]
    depth_2 [
        ^depth_2
    ]
]

Object subclass: Puzzle02 [
    | commands |
    Puzzle02 class >> new [
        ^super new init ; yourself
    ]
    init [
        | f filename |
        commands := OrderedCollection new.
        filename := Smalltalk arguments at: 1.
        f := FileStream open: filename mode: FileStream read.
        f linesDo: [ :line | commands add: (self commandFrom: line). ].
        f close.
    ]
    solve [
        | submarine |
        submarine := Submarine new.
        commands do: [ :command | submarine execute: command ].
        ^{ (submarine hpos) * (submarine depth_1).
           (submarine hpos) * (submarine depth_2) }
    ]
    commandFrom: line [
        | parts |
        parts := line substrings.
        ^Dictionary from: { #direction -> parts first.
                            #value -> parts last asNumber }
    ]
]

results := Puzzle02 new solve.
Transcript show: (results first) asString ; nl.
Transcript show: (results last) asString ; nl.
