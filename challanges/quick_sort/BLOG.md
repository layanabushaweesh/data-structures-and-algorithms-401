## Quick Sort

quiick sort is similar to merge sort, in that it's a conquer and divide style sorting algorythm.
It chooses a pivot value and partitions the input array into a left and right array.
The main difference between merge sort and quick sort is that by the time quick sort has broken up the array into sub arrays of single elements the array is sorted.

## Pseudocode
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

### Trace the code
array = [1, 8, 2, 10, 4, 5,6]

Index: 0 1 2 2 4 5 6

low = 0,
high = 6,
pivot = array[h] =6
i = -1

Traverse from 
j = low to high-1
j = 0 : Since array[j] <= pivot
do i++ and swap array[i], array[j]
i = 0

array = [1, 8, 2, 10, 4, 5,6] 
i and j are the same no change

j = 1 
Since array[j] > pivot
No change 

j = 2 
Since array[j] <= pivot
iterate i and swap
array[i], array[j]
i = 1
array = [1, 2, 8, 10, 4, 5,6] We swap 8 and 2

j = 3 : Since array[j] > pivot
No change 

j = 4 : Since array[j] <= pivot
iterate i and swap array[i], array[j]

i = 2

array = [1, 2, 4, 10, 8, 5,6] we swap 8 and 4 

j = 5 : Since array[j] <= pivot 
iterate and swap array[i] with array[j] 
i = 3
array = [1, 2, 4, 5, 8, 10,6] we swap 10 and 5 

j == high-1,
break the loop
at the end place pivot at correct position by swapping
array[i+1] and array[high] 

array = [1, 2, 4, 5,6, 10, 8]we swap 8 and 10 
array=[1,2,4,5,6,8,10]