## Insertion Sort:

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms .

## Pseudocode:

InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

## Trace the code:

sample array [8,4,23,42,16,15]

 ![image](1.png)

 ![image](2.png)

 ![image](33.png)

 ![image](4.png)

 ![image](5.png)

so the output array will be [4,8,15,16,23,42] sorted from lowest number to highest number by insertion sort method

