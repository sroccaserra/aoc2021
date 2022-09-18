Object subclass: Puzzle01 [
    | numbers |
    Puzzle01 class >> new [
        <category: 'instance creation'>
        | r |
        r := super new.
        r init.
        ^r
    ]
    init [
        <category: 'initialization'>
        | f filename |
        numbers := OrderedCollection new.
        filename := Smalltalk arguments at: 1.
        f := FileStream open: filename mode: FileStream read.
        f linesDo: [ :line | numbers add:(line asNumber). ].
        f close.
    ]
    solve1 [
        <category: 'solving'>
        | result previous |
        result := 0.
        previous := 9999.
        numbers do: [ :n | previous < n ifTrue: [ result := result + 1 ].
                           previous := n ].
        ^result
    ]
    solve2 [
        <category: 'solving'>
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
]

p := Puzzle01 new.
Transcript show: p solve1 asString ; nl.
Transcript show: p solve2 asString ; nl.
