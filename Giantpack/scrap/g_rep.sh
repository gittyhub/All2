#!/bin/bash

#grep -o '.\{0,50\}$.\{0,4\}' test2 > test3

#grep -o '*$.\{0,4\}' test2 > test3
#grep -o '.\{0,30\}$[[:digit:]]*\.[[:digit:]].\{0,30\}' test2 > test3
#grep -o '.\{0,90\}8[/][[:digit:]]*[/][[:digit:]]*.\{0,90\}' test2 > test3
grep -o '.\{0,90\}8[/][[:digit:]]*.\{0,90\}' test2 > test3

#sort test3 > test4
