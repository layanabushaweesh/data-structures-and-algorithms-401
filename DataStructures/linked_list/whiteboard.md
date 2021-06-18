## Code Challenge Whiteboarding
Problem Domain:

Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list.

## In/Out

ll.kthFromEnd(k)

Input ll                                	Arg k	 Output
 head -> [1] -> [3] -> [8] -> [2] -> X    	0	       2
 head -> [1] -> [3] -> [8] -> [2] -> X   	2	       3
 
## Edge cases:
Empty array
Null
Not an array

## Visulization

Input ll                                	Arg k	 Output
 head -> [1] -> [3] -> [8] -> [2] -> X    	0	       2
index =>    3     2     1      0
 => when we start the index value from the end of the list index[0]=2

## Big-O: O(N) 

linear relation

## Algortihm:

function that take a value of k ,
we loop and add every value to the list , 
if k=0 return the last element in the list,
else we return value at index [(k*-1)-1]

## Pseudo Code

define a function that take a value of k ,
if k is negative return Can't be negative
if k not a number return should be numbers only
define emty list add every value to the list
if k-0  return the last number in list
if k >= lenght of list return error
else return value at index [(k*-1)-1]

## Code

  
```
        def kthFromEnd(self,k):

        if k<0:
            return "Can't be negative"
        if type(k)!=type(1):
            return 'should be numbers only'
        
        list=[]
        current = self.head
        while current:
            list+=[current.value]
            
            current=current.next
        if k==0:
            return list[-1]
        else:
            if k>=len(list):
                return 'error'
            return list[(k*-1)-1]
  
```



## Verification:

```
        def kthFromEnd(self,k):  ... k=0

        if k<0:
            return "Can't be negative"
        if type(k)!=type(1):
            return 'should be numbers only'
        
        list=[] ...........  list =[1,2,3,4]
        current = self.head
        while current:
            list+=[current.value]
            
            current=current.next
        if k==0:    ................true 
            return list[-1].............return 4  #last element
        else:
            if k>=len(list):
                return 'error'
            return list[(k*-1)-1]
```