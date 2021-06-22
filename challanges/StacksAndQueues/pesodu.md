## Code Challenge Whiteboarding
Problem Domain:

is to build a queue data structure behavior for a Pseudo Queue class using two Stacks instead of using front and rear parameters as in queue. 
the results of enqueue and dequeue in the Pseudo Queue should be the same process in Queue.


## In/Out & Visulization

enqueue(value)

Input	                 Args	         Output
[10]->[15]->[20]         5	             [5]->[10]->[15]->[20]

dequeue()
Input	                    Output	        Internal State
[5]->[10]->[15]->[20]	    20          	[5]->[10]->[15]
 
## Edge cases:
Empty array Null Not an array



## Big-O: O(N) 

linear relation

## Algortihm:
enqueue(value):
use push method to stack directlly
dequeue():
revers the stack and push it to empty one
use pop for revers the stack to remove the first element
revers the stack again to back to original


## Pseudo Code
define Pseudo_Queue class and have stack1 & stack2 attribute
define enqueue method which take a value and push it to stack1
define  method which didnt take argument we assign a new stack and push value to it
then we use pop method then we back the original form to the stack. 

## Code

  
```
 class Pseudo_Queue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,value):

        """
        this method
        which inserts value into the PseudoQueue

        """
        return self.stack1.push(value).__str__
        

    def define(self):

        """
        this method
        which extracts a value from the PseudoQueue

        """
        
        stack = Stack()
      # revers the stack
        while self.stack.top:   
            stack.push(self.stack.pop())
     # remove the Top
        output = stack.pop()  

        while stack.top:
            self.enqueue(stack.pop())

        return output.__str__

    def __str__(self):

        return str(self.stack)
        # return str(self.stack2)       
  
```



## Verification:

```
  class Pseudo_Queue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,value):

        """
        this method
        which inserts value into the PseudoQueue

        """
        return self.stack1.push(value).__str__
        

    def dequeue(self):

        """
        this method
        which extracts a value from the PseudoQueue

        """
        
        stack = Stack()
      # revers the stack
        while self.stack.top:   
            stack.push(self.stack.pop())
     # remove the Top
        output = stack.pop()  

        while stack.top:
            self.enqueue(stack.pop())

        return output.__str__

    def __str__(self):

        return str(self.stack)
        # return str(self.stack2)         
```