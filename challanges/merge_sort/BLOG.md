## Merge Sort

### Description

Merge sort is a divide and conquer sorting algorithm. 
It recursively splits each portion of array until it's comparing only two arrays .
It then merges the sorted subarrays back again.

### Pseudocode

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

### Trace
1. INPUT ARRAY: [4, 2, 30, 4, 16, 1, 20, 12]

2. Split ints into 2 half: L and A

3. L [4, 2, 30, 4]
   A [16, 1, 20, 12]

4. Call mergesort on L, 
   which will continue to split the lists in half until only one element 
      [4, 2, 30, 4]
      [4, 2,]
      [4], [2]

5. Once the left most pair has been split, 
   stitch back together 
   [4], [2] will be [2, 4]

6. the same process  for the right half of L,
   [30, 4] [30], [4] will be [4, 30]

7. Stitch L backtogether  [2, 4, 4, 30]


8. Repeat the  process for A [16, 1, 20, 12]

   [16, 1, 20, 12]

   [16, 1]

   [16], [1] will be [1, 16]

   [20, 12]
   [20], [12] WILL BE [12, 20]

9. Merge R  [1, 12, 16, 20]

Merge L  and A THE SORTED ARRAY =>[1, 2, 4, 4, 12, 16, 20, 30]
