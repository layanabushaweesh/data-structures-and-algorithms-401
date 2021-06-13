from linkedlist import LinkedList

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
    ll.append(3)
    ll.__str__()
    assert ll.__str__() == "{ 1 } -> { 2 } -> { 3 } -> NULL"

######## code challange 6 ##########

def test_append_2():  
    ll = LinkedList()
    ll.append(2)
    assert ll.head.value == 2

def test_insertBefore():  
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.insert(9)
    assert ll.__str__().insertBefore(
        2 , 8) == " { 9 } -> { 1 } -> { 8 } -> { 2 } -> { 3 } -> { 4 }  -> NULL "
        


def test_insertAfter():  
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert(9)
    assert ll.__str__().insertAfter(
        2, 8) == " { 9 } -> { 1 } -> { 2 } -> { 8 } -> { 3 }  -> NULL "



