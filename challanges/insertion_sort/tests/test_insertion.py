from challanges.insertion_sort.insertion import InsertionSort

def test_insertion_Sort():
    assert InsertionSort([5,4,23,15,20,30]) == [4, 5, 15, 20, 23, 30]
    assert InsertionSort([2,18,12,80,52,-2]) == [-2, 2, 12, 18, 52, 80]
 
    
