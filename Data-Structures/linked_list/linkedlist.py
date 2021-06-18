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

    def insert_before(self,value,new_value):

        """
        input                               arguments            output
        head -> [1] -> [3] -> [2] -> X   	3, 5	             head -> [1] -> [5] -> [3] -> [2] -> X

        this function will add new value befor spicific place

        """
        node = Node(new_value)

        current=self.head

        if current.new_value == value:
            self.insert(new_value)

        else :
            while current.next.new_value != value:
                  current=current.next

            else:

                node.next=current.next
                current.next=node
            
    def insert_after(self, value, new_value):

        """

        input                                  arguments         output
        head -> [1] -> [3] -> [2] -> X      	3, 5	          head -> [1] -> [3] -> [5] -> [2] -> X
        
        this function will add new value after spicific place

        """
        node =  Node(new_value)

        current=self.head

        while current:

         if current.value == value:
            node.next=current.next
            current.next = node

            break
         current=current.next


 ######## code challange 8 ##########
def zipLists(list1,list2):
    
    if not (list1 and list2) :
        # check the list is exists
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