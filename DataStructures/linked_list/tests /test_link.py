from DataStructures.linked_list.linkedlist import LinkedList

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
    assert ll.__str__() == "{1} ->{2} ->{3} ->NULL"

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
    assert ll.insertBefore(
        2 , 8) == "{9} ->{1} ->{8} ->{2} ->{3} ->{4} ->NULL"
        


def test_insertAfter():  
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert(9)
    assert ll.insertAfter(
        2, 8) =="{9} ->{1} ->{2} ->{8} ->{3} ->NULL"

def test_insertBefore_mid(): 
    ll = LinkedList()
    ll.append('layan')
    ll.append('lelian')
    ll.append('leen')
    ll.insert('lelia')
    actual = ll.insertBefore('layan', 'madleen')
    excepted = "{'lelia'} ->{'madleen'} ->{'layan'} ->{'lelian'} ->{'leen'} ->NULL"
    assert actual == excepted

def test_insertafter_mid(): 
    ll = LinkedList()
    ll.append('layan')
    ll.append('lelian')
    ll.append('leen')
    ll.insert('lelia')
    actual = ll.insertAfter('layan', 'madleen')
    excepted = "{'lelia'} ->{'layan'} ->{'madleen'} ->{'lelian'} ->{'leen'} ->NULL"
    assert actual == excepted


def test_insertBefore_last(): 
    ll = LinkedList()
    ll.append('layan')
    ll.append('lelian')
    ll.append('leen')
    ll.insert('lelia')
    actual = ll.insertBefore('leen', 'madleen')
    excepted = "{'lelia'} ->{'layan'} ->{'lelian'} ->{'madleen'} ->{'leen'} ->NULL"
    assert actual == excepted

def test_insertafter_last(): 
    ll = LinkedList()
    ll.append('layan')
    ll.append('lelian')
    ll.append('leen')
    ll.insert('lelia')
    actual = ll.insertAfter('leen', 'madleen')
    excepted = "{'lelia'} ->{'layan'} ->{'lelian'} ->{'leen'} ->{'madleen'} ->NULL"
    assert actual == excepted

def test_insertafter_first(): 
    ll = LinkedList()
    ll.append('layan')
    ll.append('lelian')
    ll.append('leen')
    ll.insert('lelia')
    actual = ll.insertAfter('lelia', 'madleen')
    excepted = "{'lelia'} ->{'madleen'} ->{'layan'} ->{'lelian'} ->{'leen'} ->NULL"
    assert actual == excepted



    
######## code challange 7 ##########
def test_k_greater_than_linked_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kthFromEnd(10)
    expected='error'
    assert actual==expected
    
def test_k_same_the_linked_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kthFromEnd(4)
    expected='error'
    assert actual==expected
    
    

def test_k_not_postive_intger():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    actual = ll.kthFromEnd(-1)
    expected="can't be negative"
    assert actual==expected
    
    

def test_k__path():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    actual = ll.kthFromEnd(2)
    expected=2
    assert actual==expected