#Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
from typing import Counter


class Node:
    def __init__(self, value):
        # Assign data
        self.value = value 
        # Initialize next as null
        self.next = None 

# Within your LinkedList class, include a head property.

class LinkedList:
    def __init__(self):
        # Initial the head as None
        self.head = None 

    def insert(self,value):
        """
        this method to add element
        to head of the list

        """
        # Create a new Node
        node = Node(value) 
        node.next=self.head
        self.head=node

    def include(self, value):

        """
        Return T/F if value is in the linked list or not
        input value 
        output boolean

        """
        current =self.head
        while current != None:
            if current.value == value:
               return True #found data
            current=current.next

        else : #not found
             return False

    
        
    def __str__(self):

     """
        this method will 
        Loop over all nodes
        print all values in one line
        "{ a } -> { b } -> { c } -> NULL"

     """
     current =self.head
     output_string=""
     while current:
         output_string +=f"{ {str(current.value)} } ->" # always str return a string
         current=current.next
     return output_string 

     
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


if __name__ == "__main__":
    ll = LinkedList()
    # Instances of Node
    n1 = Node(1)
    n2 = Node(2)

  
# add lolo at the first node on head:
    ll.insert('lolo')

# add 9 at the end of list:
    ll.append(9)

# return true or fals if the value include in the list => should return true
    ll.include(1)
  

# print all value in one line
    print(ll.__str__())