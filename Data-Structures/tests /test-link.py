from linked_list.linkedlist.py import LinkedList

def test_append_1():  
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value == 1

def test_insert_1():  
    ll = LinkedList()
    ll.insert('lolo')
    ll.insert('lulu')
    assert ll.head.value == 'lulu'

def test_insert_2():  
    ll = LinkedList()
    ll.insert('lolo')
    assert ll.head.value == 'lolo'

def test_include_1():  
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    assert ll.include(1) == True

def test_include_2():  
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    assert ll.include(7) == False


def test_str():  
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.__str__()
    assert ll.__str__() == " 1-> 2 -> NULL "



