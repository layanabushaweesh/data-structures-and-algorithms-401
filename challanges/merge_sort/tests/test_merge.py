from challanges.merge_sort.merge_sort import Mergesort
def test_merge_sort_0():
    a = [8,4,8,42,50,90]
    Mergesort(a)
    assert a ==  [4, 8, 8, 42, 50, 90]
    b = [20,50,12,100,5,-20]
    Mergesort(b)
    assert b ==  [-20, 5, 12, 20, 50, 100]