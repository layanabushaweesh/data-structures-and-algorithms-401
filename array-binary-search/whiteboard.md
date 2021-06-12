# Code Challenge Whiteboarding
## Problem Domain

Write a function which takes in 2 parameters: a sorted list and the search key. return the index of the list’s element that is equal to the value of the search key, or -1 if the element is not in the list.

## In/Out

Input: list of n elements and separate value Output: index of the list’s element that is equal to separate value

Edge cases: Empty list Null Not an list

## Visulization
Input : [4, 8, 15, 16, 23, 42], 15 Output : 2

Input :[-131, -82, 0, 27, 42, 68, 179], 42 Output : 4

Input: [11, 22, 33, 44, 55, 66, 77], 90 Output : -1

## Big-O:
O(N) linear relation.

## Algortihm:

we will write a function that will loop through the list and divide the list into two half and check for the index for separate value if it is found and return it , if it didn't found return -1

## Pseudo Code

define function(list,key): first_index=0 last_index=lenght(list)-1 loop in the list while first_index less or equal last_index: middle_index=(first_index+last_index)/2 then we keep loop in the list until we find the index of the key in the list -1 will return if not found the key

## Code

def BinarySearch(list, key): first_index = 0 last_index = len(list) - 1

while first_index <= last_index:

    middle_index = (last_index + first_index) // 2

    if list[middle_index] < key:
        first_index = middle_index + 1

    if list[middle_index] > key:
        last_index = middle_index - 1

    else:
        return middle_index

return -1


 ## Verification

Input : list=[4, 8, 15, 16, 23, 42] output: 2 key=15

def BinarySearch(list, key): first_index = 0 ... last_index = len(list) - 1 ... last_index =6-1=5

while first_index <= last_index:  .... 0<= 5 (true)

    middle_index = (last_index + first_index) // 2   ... middle_index=2

    if list[middle_index] < key: .... this false statement will not implement because  list[2] =15 and 15 = key value
        first_index = middle_index + 1

    if list[middle_index] > key:   ... this false statement too
        last_index = middle_index - 1

    else:    ... this will implement and return 2 and that's what we want    #
        return middle_index

return -1