## Code Challenge Whiteboarding
Problem Domain:
Write a function called zipLists which takes two linked lists as arguments.
Zip the two linked lists together into one so that the nodes alternate between the two lists
and return a reference to the head of the zipped list.

## In/Out
zipLists(list1, list2)

Arg list1	                     Arg list2                        Output
head -> [1] -> [3] -> [2] -> X	 head -> [5] -> [9] -> [4] -> X	  head -> [1] -> [5] -> [3] -> [9] -> [2] -> [4] -> X
head -> [1] -> [3] -> X          head -> [5] -> [9] -> [4] -> X    head -> [1] -> [5] -> [3] -> [9] -> [4] -> X

## Edge cases:
the lists are empty

## Big-O: O(N) 
o(N)

## Algortihm:
 1. check the list is exists
 2. get the head of each list
 3. append value  from list 1 and value from list 2 in a loop in outputlist
 4. return the output list 

## Pseudo Code

1.define a function that take two lists
2.if list is empty return list 1
3.make a new list
4.assigen value to head of list 1 &
5.assigen value to head of list 2 
6.each time we loop we append value from list 1 then value from list 2
4.return new list as string



## Code

```
     def zipLists(list1,list2):
        
        if not (list1 and list2) :
         # check the list if exists
            return list1 
        
        output_list =LinkedList()
        #get the head of each list
        value_one =list1.head
        value_two =list2.head
        #append value one the value two in a loop
        while value_one:
            output_list.append(value_one.value)
            if value_two:
                output_list.append(value_two.value)
                value_two = value_two.next
            value_one= value_one.next
        while value_two :
            output_list.append(value_two.value)
            value_two =value_two.next
            #return the output list as ast
        return output_list.__str__() 
  
```

## Verification

  
```
  def zipLists(list1,list2):
                                                           
        if not (list1 and list2) :                  ...  list1=[1] -> X    list2= [9]  -> X   out=[1] -> [9] -> X
         # check the list if exists   
            return list1 
        
        output_list =LinkedList()              .......new empty linkedlist      
        #get the head of each list             
        value_one =list1.head                      ....value_one=1
        value_two =list2.head                      .....value_two=9
        #append value one the value two in a loop
        while value_one:
            output_list.append(value_one.value)  ....  output list=[1] -> X
            if value_two:
                output_list.append(value_two.value)    ....output list= [1] -> [9] -> X
                value_two = value_two.next         
            value_one= value_one.next            
        while value_two :
            output_list.append(value_two.value)   
            value_two =value_two.next
            #return the output list as ast  .....output list= [1] -> [9] -> X
        return output_list.__str__()               { 1 } -> { 9 } ->  NULL
```
