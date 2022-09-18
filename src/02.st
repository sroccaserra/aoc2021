AOCObject subclass: Submarine [
    | hpos depth_1 depth_2 aim |
    initialize [
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

AOCObject subclass: Puzzle02Solver [
    | commands |
    initialize [
        commands := OrderedCollection new.
    ]
    solve [
        | submarine |
        submarine := Submarine new.
        commands do: [ :command | submarine execute: command ].
        ^{ (submarine hpos) * (submarine depth_1).
           (submarine hpos) * (submarine depth_2) }
    ]
    processInputLine: line [
        | parts command |
        parts := line substrings.
        command := Dictionary from: { #direction -> parts first.
                                      #value -> parts last asNumber }.
        commands add: command.
    ]
]

solver := Puzzle02Solver new.
InputFileReader readInputFor: solver.
results := solver solve.
Transcript show: (results first) asString ; nl.
Transcript show: (results last) asString ; nl.
