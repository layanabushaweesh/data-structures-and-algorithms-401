# Stacks and Queues
<!-- Short summary or background information -->
Stack:
A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

Queue :
A Queue is a linear structure which follows a particular order in which the operations are performed.

## Challenge
<!-- Description of the challenge -->
Write specific methods inside Stack & Queue class


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

I use a basic node class with a next and a value set to none ,for the stack I create a class stack and initialize it with self and top properties then I define other methods in the class
for the queue, I create class queue and initialize it with self and front and rear properties then I define other methods in the class.

O(N) =>  linear relation


## API

<!-- Description of each method publicly available to your Stack and Queue-->
### Stack class has 4 methods:

1. pop() this method removes the item on top of the stack by .

2. push() This method pushes a new node onto the stack .

3. peek() This method returns the value at the top of the stack.

4. is_empty() Checks if its empty exists and returns a boolean.

### Queue class has 4 methods:

1. enqueue() Appends a node to the end of the queue .

2. dequeue() removes a node from the front of the queue.

3. peek() This method returns the value at the front of the queue.

4. is_empty() Checks if its empty exists and returns a boolean.


