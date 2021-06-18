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

we take value of empty array and assign
 current value to the head if k is minus will 
 return error then will append current value 
 to array then we reverse the array a
 nd return the index from the end
## Pseudo Code

array=empty arr
current = first element of the list
if k<0 return error
loop in arr and append current value
revers the arr and return the index of value from the end


## Code

  
```
        array = []
        current = self.head
        if k < 0:
            return 'error'
        if k > len(array):

            return 'error'
        while current:
            array.append(current)
            current = current.next
        array.reverse()
        if k == len(array):
            k = k -1
        return array[k].value
  
```



## Verification:

```
        array = []   
        current = self.head            ...   [1] -> [3] -> [8] -> [2]    k=0  output =2
        
        if k < 0:
            return 'error'

         if k > len(array):
            return 'error'
            
        while current:
            array.append(current)
            current = current.next    .... array=[1,3,8,2]         len=4        k=0
        array.reverse()               .... array.revers=[2,8,3,1]
        if k == len(array):            ....  index=>     0,1,2,3
            k = k -1
        return array[k].value          ....  index[0] =2 which is the output #
  
```