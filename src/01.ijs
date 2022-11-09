readfile =: 1!:1

filename =. < input  NB. the interface with the environment requires a boxed string
contents =. readfile filename
numbers =.  > 0 ". each cutopen .toJ contents

echo numbers
