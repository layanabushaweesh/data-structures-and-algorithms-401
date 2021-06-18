#Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
from typing import Counter, cast


class Node:
    def __init__(self, value):
        # Assign data
        self.value = value 
        # Initialize next as null
        self.next = None 

# Within your LinkedList class, include a head property.

class LinkedList:
    def __init__(self,value):
        # Initial the head as None
        self.head = None 
        self.node_lst = []

    def append(self, value):
        """
        Adds a node of a value to the 

        end of linked list
        """
        node =Node(value)
        if self.head == None:
            self.head=node
        else:
            current=self.head

            while current.next:
                current=current.next
            current.next=node
  

    def kth_from_end(self, k):

        """
         take in a value(k) and returns

         the Node k places away from the tail
        """
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