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
         output_string +=f"{ {(current.value)} } ->" # always str return a string
         current=current.next


            
     else:
        output_string = output_string + 'NULL'
     return output_string



     ######## code challange 6 ##########
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

    def insertBefore(self,value,new_value):

        """
        input                               arguments            output
        head -> [1] -> [3] -> [2] -> X   	3, 5	             head -> [1] -> [5] -> [3] -> [2] -> X
        this function will add new value befor spicific place
        """
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
            
    def insertAfter(self, value, new_value):

        """
        input                                  arguments         output
        head -> [1] -> [3] -> [2] -> X      	3, 5	          head -> [1] -> [3] -> [5] -> [2] -> X
        
        this function will add new value after spicific place
        """
        current = self.head
        node = Node(new_value)
        while current != None:
            if current.value == value:
                break
            current = current.next

        node.next = current.next
        current.next = node
        return self.__str__()

        ######## code challange 7 ##########
         
    def kthFromEnd(self,k):

        """
        this function take a number, k, as a parameter
        return the node value that is k from the end 
        of the linked list.

        """
        if k<0:
            return "can't be negative"
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
        


        