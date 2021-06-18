# Code Challenge Whiteboarding

## Problem Domain:

Write  this two methods for the Linked List class:
1. insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
2. insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node


## In/Out

.insertBefore(value, newVal)

Input	                         Args	    Output
head -> [1] -> [3] -> [2] -> X 	 3, 5	    head -> [1] -> [5] -> [3] -> [2] -> X


.insertAfter(value, newVal)

Input	                         Args	    Output
head -> [1] -> [3] -> [2] -> X   3, 5	    head -> [1] -> [3] -> [5] -> [2] -> X


Edge cases: Empty linkedlist Null Not an linkedlist.



## Big-O:
O(N) linear relation.

## Algortihm:
1. insertBefore function first we assign values to node and current value then we loop in linked list and add new value argument before value argument and return a ll as string.

2. insertAfter function first we assign values to node and current value then we loop in linked list and add new value argument after value argument and return a ll as string.

## Pseudo Code

1. insertBefore function:
def afuction that takes value and new value as an argument
node = Node(new_value)
current=firt value in ll
if current value = value we insert the new value else we keep loop in ll and return astring.

2. insertAfter function:
def afuction that takes value and new value as an argument
node = Node(new_value)
current=firt value in ll
we loop in ll then we assign current.next to Node(new_value) and return astring.

## Code
```
 def insertBefore(self,value,new_value):
        node = Node(new_value)

        current=self.head

        if current.value == value:
            self.insert(new_value)

        else :
            while current.next.value != value:
                  current=current.next

            else:

                node.next=current.next
                current.next=node
            return self.__str__()  

```
```
def insertAfter(self, value, new_value):

        
        current = self.head
        node = Node(new_value)
        while current != None:
            if current.value == value:
                break
            current = current.next

        node.next = current.next
        current.next = node
        return self.__str__()
```


## Verification
```
 def insertBefore(self,value,new_value):    ... Input	 head -> [1] -> [3] -> [2] -> X                     	  
                                               ... value =3        new_value=5 	    
        node = Node(new_value)  ... node=5

        current=self.head ... current=1

        if current.value == value:  .... false
            self.insert(new_value)

        else :
            while current.next.value != value:  .. 3 != 3  false
                  current=current.next

            else: ... 

                node.next=current.next  ... node.next=3
                current.next=node  ..current.next=5
            return self.__str__()       ...output   head -> [1] -> [5] -> [3] -> [2] -> X
                                           to str"{1} ->{5} ->{3} ->{2} ->NULL"

```
```
def insertAfter(self, value, new_value):  ..input head -> [1] -> [3] -> [2] -> X
                                            ...value =3        new_value=5 
        
        current = self.head   .. current=1
        node = Node(new_value) ...node=5
        while current != None: .. true
            if current.value == value: .. fals
                break
            current = current.next... current=3

        node.next = current.next ... node.next =2
        current.next = node ... current.next = 5  ..  output=[1] -> [3] -> [5] -> [2] -> X
        return self.__str__()                             to str"{1} ->{3} ->{5} ->{2} ->NULL"
                           
```
