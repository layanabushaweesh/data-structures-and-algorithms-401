def Mergesort(array):

    n = len(array)

    if n > 1:
      mid = int(n//2)

      right = array[mid:]
      left = array[0:mid]


      Mergesort(right)
      Mergesort(left)


      Merge(left, right, array)

def Merge(left, right, array):
    k = 0
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:

            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
            array[k] = left[i]

            k += 1
            i += 1
    while j < len(right):
        
            array[k] = right[j]
            k += 1
            j += 1
    return array