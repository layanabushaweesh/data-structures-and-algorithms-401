from challanges.quick_sort.quicksort import QuickSort

def test_quicksort():
    array = [100,4,-2,42,50,15]
    QuickSort(array,0,len(array)-1)
    assert array == [-2, 4, 15, 42, 50, 100]