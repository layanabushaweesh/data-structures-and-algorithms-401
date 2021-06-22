## Code Challenge Whiteboarding
Problem Domain:

write function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced.

## In/Out
input is asting
output is a boolean

## Edge cases:
different type input

## Visulization
Input	                Output
{}                  	TRUE
{}(){}               	TRUE
[({}]	                FALSE

## Big-O: O(N) 

linear relation

## Algortihm:
create a function that take one argument as an input
write three if statement to check user input if it contain brackets
return true else return false

## Pseudo Code
define function(argument):
if () in argument return true
if {} in argument return true
if []in argument return true
else 
return false

## Code
```
   if '(' in str_input and ')' in str_input:
        return True
    if '{' in str_input and '}' in str_input:
        return True

    elif '[' in str_input and ']' in str_input:
        return True

    else:
        return False
```
   

## Verification:

```                                               str_input=()
   if '(' in str_input and ')' in str_input:   ...........this true statment
        return True
    if '{' in str_input and '}' in str_input:
        return True

    elif '[' in str_input and ']' in str_input:
        return True

    else:
        return False
```
