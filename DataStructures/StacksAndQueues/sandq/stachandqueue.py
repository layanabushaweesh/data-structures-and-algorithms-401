
#Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#Create a Stack class that has a top property. It creates an empty Stack when instantiated.

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):

        """
        this function
        which takes any value as an argument 
        and adds a new node with that value 
        to the top of the stack
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):

        """
        this function
        removes the node from the top 
        of the stack, and returns the 
        node’s value.

        """
        if self.top:
            self.top = self.top.next
            return self.top.value
        else:
            #raise exception
            return "empty stack"

    def peek(self):

        """
        this function
        returns the value of the node located
        on top of the stack, without removing 
        it from the stack.

        """
        if self.top:
                
          return self.top.value
        else:
          #raise exception
            return "empty stack"

    def is_empty(self):

          """
          this function
          returns a boolean indicating 
          whether or not the stack is empty.
          
          """
          return True if self.top is None else False


#Create a Queue class that has a front property. It creates an empty Queue when instantiated.
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):

        """
        this function
        takes any value as an argument
        and adds a new node with that 
        value to the back of the queue 

        """
        # front is first value rear is last value
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):

        """
        this function
        does not take any argument,
        removes the node from the front
        of the queue, and returns the node’s value 

        """
        if self.is_empty():
            #raise exception
            return 'empty queue'
        else:
            # remove first value
            self.front = None
            #current value is the last value
            current = self.rear

            while current.next != None:

                current = current.next
                self.front = current
     

    def peek(self):

        """
        this function
        returns the value of the node located in 
        the front of the queue, without removing 
        it from the queue.

        """
        return self.front.value

    def is_empty(self):

        """
        this function
        returns a boolean indicating whether
        or not the queue is empty.
        """
        return True if self.front is None else False
