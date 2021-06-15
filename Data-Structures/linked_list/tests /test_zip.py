from linked_list.linkedlist import LinkedList, zipLists

def test_zipLists_1(): 
    list1 = LinkedList() 
    list1.append(1) 
    list1.append(2) 
   
    list2 = LinkedList() 
    list2.append(4) 
    list2.append(5) 
    
    assert zipLists(list1,list2) == "{ 1 } -> { 4 } -> { 2 } -> { 5 } -> NULL"




def test_zipLists_2(): 
    list1 = LinkedList() 
    list1.append(1) 
    list1.append(2) 
  
 
    list2 = LinkedList() 
    list2.append('a') 
    list2.append('b') 
    list2.append('c')

    assert zipLists(list1,list2) == "{ 1 } -> { a } -> { 2 } -> { b } -> { c } -> NULL"




