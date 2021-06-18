from ll-kth-from-end.linkedlist import LinkedList




def test_k_greater():
    ll = LinkedList()
    ll.append('1')
    ll.append('2')
    print(ll.node_lst)
    actual = ll.kth_from_end(10)
    excepted = 'error'
    assert actual == excepted



