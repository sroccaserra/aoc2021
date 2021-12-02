#!/usr/bin/env bash

n=$(printf %02d "$1")

if test "$2" != "test"
then
    sed "s/X/$1/" "XX.hs" > "src/${n}.hs"
else
    sed "s/XX/$n/" "XXSpec.hs" > "src/${n}Spec.hs"
fi

stack build --only-dependencies
