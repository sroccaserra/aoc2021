AOCObject subclass: Puzzle01Solver [
    | numbers |
    initialize [
        numbers := OrderedCollection new.
    ]
    solve1 [
        | result previous |
        result := 0.
        previous := 9999.
        numbers do: [ :n | previous < n ifTrue: [ result := result + 1 ].
                           previous := n ].
        ^result
    ]
    solve2 [
        | result p1 p2 p3 |
        result := 0.
        p1 := 9999.
        p2 := 9999.
        p3 := 9999.
        numbers do: [ :n | (p1 + p2 + p3) < (n + p1 + p2) ifTrue: [ result := result + 1 ].
                           p3 := p2.
                           p2 := p1.
                           p1 := n ].
        ^result
    ]
    processInputLine: line [
        numbers add: (line asNumber).
    ]
]

solver := Puzzle01Solver new.
InputFileReader readInputFor: solver.
Transcript show: solver solve1 asString ; nl.
Transcript show: solver solve2 asString ; nl.
