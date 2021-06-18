from DataStructures.linked_list.linkedlist import LinkedList , zipLists

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
        
######## code challange 8 ##########


def test_zipLists_1(): 
    list1 = LinkedList() 
    list1.append(1) 
    list1.append(2) 
   
    list2 = LinkedList() 
    list2.append(4) 
    list2.append(5) 
    
    assert zipLists(list1,list2) == "{1} ->{4} ->{2} ->{5} ->NULL"




def test_zipLists_2(): 
    list1 = LinkedList() 
    list1.append(1) 
    list1.append(2) 
  
 
    list2 = LinkedList() 
    list2.append('a') 
    list2.append('b') 
    list2.append('c')

    assert zipLists(list1,list2) == "{1} ->{'a'} ->{2} ->{'b'} ->{'c'} ->NULL"

def test_zipLists_3(): 
    list1 = LinkedList() 
    list1.append('layan') 
    list1.append('lelian')
    list1.append('laila') 
  
 
    list2 = LinkedList() 
    list2.append('madline') 
    list2.append('lili') 
    

    assert zipLists(list1,list2) == "{'layan'} ->{'madline'} ->{'lelian'} ->{'lili'} ->{'laila'} ->NULL"

def test_zipLists_4(): 
    list1 = LinkedList() 
    list1.insert(9) 
    list1.append(2) 
   
    list2 = LinkedList() 
    list2.append(4) 
    list2.append(5) 
    
    assert zipLists(list1,list2) == "{9} ->{4} ->{2} ->{5} ->NULL"
