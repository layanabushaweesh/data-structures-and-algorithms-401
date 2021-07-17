


class Node:
    def __init__(self,value):
        self.value=value
     
        self.next=None



class linkedlist():
    def __init__(self):
     self.head=None

    def add(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
        else:
           current =self.head
           while current.next:
                 current=current.next
           current.next=node 


    def __str__(self):
        current = self.head
        value = []
        while current:
            value.append(current.value)
            current = current.next
        return f"{value}"


    def value(self):
    
        value = []
        current = self.head
        while current:
            value.append(current.value)
            #keep looping
            current = current.next
        return value