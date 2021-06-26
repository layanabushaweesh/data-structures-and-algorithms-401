# Trees
<!-- Short summary or background information -->
### Trees
are non-linear data structure that represent nodes connected by edges.
Each tree consists of a root node as the Parent node,
and the left node and right node as child nodes.

### Binary tree
A tree whose elements have at most two children is called a binary tree.
Each element in a binary tree can have only two children.
A node’s left child must have a value less than its parent’s value, 
and the node’s right child must have a value greater than its parent value.

## Challenge
<!-- Description of the challenge -->

1. Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

2. Create a Binary Tree class that has three methods, pre order, in order, and post order

3. Create a Binary Search Tree class that has two methods, add and Contains
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->


## API
<!-- Description of each method publicly available in each of your trees -->
Node class:
Node class is responsible for creating new nodes
that has a value, a right and a left defined as None

the Tree class has three methods:

pre_order method: in this method the root has to be  at first then left then right.

in_order: we start from the farthest node to the left, and  then the  the root, then the right nodes.

post_order: we start from the farthest node to the left, and then to the right, finally, we reach the root.