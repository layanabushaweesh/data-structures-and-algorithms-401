# Singly Linked List
 ## Short summary 
 The linked list is alternative to an array-based structure. A linked list is collection of nodes that collectively form linear sequence. In a singly linked list, each node stores a reference to an object that is an element of the sequence, as well as a reference to the next node of the list. It does not store any pointer or reference to the previous node. To store a single linked list, only the reference or pointer to the first node in that list must be stored. The last node in a single linked list points to nothing.

## Challenge

Create a node class that has properties for the value stored in the Node,
and a pointer to the next node class.
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
and create many methods in the linked list class.


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->


## API
1. append function :
 which takes any value as an argument and add the new node with that value to the end of the list with an O(n) Time performance.

2. insert function :
 which take any value as an argument and adds a node of a value to the head of LL with an O(1) Time performance.

3. includes function :
 which take any value as an argument and Return T/F if value is in the linked list or not

4. str function :
 which dose not take an arguments and returns a string representing all the value in the Linked List.

5. insert_before function :
  this function will add new value befor spicific place

6.  insert_after function :
  this function will add new value after spicific place
