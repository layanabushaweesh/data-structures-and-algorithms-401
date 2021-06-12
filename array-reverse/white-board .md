## Code Challenge Whiteboarding
Problem Domain:
Reverse an array without 
using any built in function

## In/Out
Input: Array of n elements 
Output: Array that reversed

## Edge cases:
Empty array
Null
Not an array

## Visulization
In: [1,2,3,4]

Out: [4,3,2,1]

In: []

Out: []

## Big-O: O(N) 

linear relation

## Algortihm:

Loop in the array
For every loop swap the current index with the alternative from the end index
Stop when reach the middle.

## Pseudo Code

Define i=0 and
 x=len(a)-1 and
  input array
while i<x:
swap a[i] and a[x]
i++
x--

## Code

  def reverse_array(array): 
    if not( type(array) == type([]) ): 
      return ' there is an error' 
    i = 0 
    x = len(array)-1 
    while i<x: 
      array[i], array[x] = array[x], array[i]
      i += 1 
      x -= 1 
    return array 



Verification:
In: a = [1,2,3,4] expected Out: [4,3,2,1,]

i = 0 x = 4-1 = 3 while 0<3: #True a[0], a[3] = a[3], a[0] a = [4,2,3,1] 

i = 0+1 = 1
x = 3-1 = 2

i = 1 x = 2 while 1<2: # True a[1], a[2] = a[2], a[1] a = [4,3,2,1] 
i = 1+1 = 2 
x = 2-1 = 1

while 2 < 1: # False Stop

return [4,3,2,1] #

