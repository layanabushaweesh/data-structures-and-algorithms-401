# Code Challenge Whiteboarding
## Problem Domain:
write a function that takes list and value to be added instead of the center index.

## In/Out
Input: list of n elements and separate value Output:list and separate value in the middle of the list

Edge cases: Empty array Null Not an array


## Visulization
Input [2,4,6,-8], 5 Output [2,4,5,6,-8]

Input [42,8,15,23,42], 16 Output [42,8,15,16,23,42]

## Big-O:
O(N) linear relation.

## Algortihm:
define a function that take a list and number as an arguments then we check if the length of array is even then specific the middle of the list also do that even the length is odd then we put the number at the middle.


## Pseudo Code
define function(list and number) if the Modulus of the lenght and 2 equal zero then middle will be Floor division for the lenght and 2 else the middle will be Floor division for the lenght and 2 + 1 then insert the number in the middle by use the middle as index number.


## Code
def insert_shift_array(list, num):

if len(list) % 2 == 0:
    middle = len(list) // 2
else:
    middle = ( len(list) // 2 )+ 1    
list[middle] = [num]
return list


## Verification
In: a =[2,4,6,-8], 5 expected Out: [2,4,5,6,-8]

def insert_shift_array(a, 5):

if len(list) % 2 == 0:     .... it will be true
    middle = len(list) // 2  .... the middle =2
else:
    middle = ( len(list) // 2 )+ 1    ... this sentance will not implement
list[middle] = [num]   ..... add 5 at index 2
return a    .... a will  be [2,4,5,6,-8] #