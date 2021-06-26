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
[({}]	                FALSE
(](	                    FALSE
{(})                 	FALSE

## Big-O: O(N) 

o(n^2)

## Algortihm:

use an empty list so we can push or pop
define an object have open an close bracket
check if bracket is open we will push it
check if bracket is close we will pop it and if bracket not equal return false
and if list still have charachter return false
other wise retyrn true
 
## Pseudo Code
define empty list
define object have keys of close bracket and values of open braket
if bracket is open push it to list
if it  close use pop() and check if bracket  not equal retuen false
if list  have charachter return false
else  retyrn true

## Code
```
  def multi_bracket_validation(str_input):
  
    list = [] 

    brackets = {'}':'{', ']':'[', ')':'('}
    for braket in str_input: 
        # check open bracket add it to list
        if braket in brackets.values(): 
            list.append(braket)
        # check closed bracket
        if braket in brackets.keys(): 
            bracket = list.pop() 
            if brackets[braket] != bracket:
                return False
    # if list still have charachter return false
    if list:
        return False
    return True
```
   

## Verification:

```                                               
  def multi_bracket_validation(str_input):
  
    list = []                                   ..............str_input='{}'
    brackets = {'}':'{', ']':'[', ')':'('}
    for braket in str_input:                           
        # check open bracket add it to list
        if braket in brackets.values(): .........
            list.append(braket) ...............list=['{']
        # check closed bracket
        if braket in brackets.keys(): 
            bracket = list.pop() .......list will be empty
            if brackets[braket] != bracket:.......false will not implement
                return False
    # if list still have charachter return false
    if list:
        return False
    return True...............................................will return true
```
