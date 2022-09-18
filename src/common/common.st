Object subclass: InputFileReader [
    InputFileReader class >> readInputFor: aPuzzleSolver [
        | f filename |
        filename := Smalltalk arguments at: 1.
        f := FileStream open: filename mode: FileStream read.
        f linesDo: [ :line | aPuzzleSolver processInputLine: line ].
        f close.
    ]
]

Object subclass: AOCObject [
    AOCObject class >> new [
        ^super new initialize ; yourself
    ]
    initialize [
        <category: 'initialization'>
        <comment: 'Initialize the object to its default state. This is typically used in a convention that the class implements the `#new` method to call `#initialize` automatically. This is not done for all objects, but the initialize method is provided here so that subclasses can call `super initialize` and not get an exception.'>
    ]
]
