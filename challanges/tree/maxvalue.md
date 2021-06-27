# Code Challenge Whiteboarding
## Problem Domain:

Find the Maximum Value in a Binary Tree


## Edge cases:
tree is empty
not numeric tree

## Visulization
Input
           5
      8          9
   10   12    3    8

Output
12

## Big-O:
O(N) linear relation.

## Algortihm:

we will check if thr root in the tree is empty or not
assum the maxs value is the root
compare the max value with left and right value
if there is value big than root value update it
return the max value

## Pseudo Code:

define max value function that didnt take argument
if the root is empty return "tree is empty"
max value = root value
define inner function that talk node value
if node is none return error
if node value big than max value
max value equal to node value 
keep checking in left an right value
return max value



## Code
```
  def max_value(self):

        if not self.root:
            return "trss is empty "
        max_val=self.root.value
        
        def max(node):
            nonlocal max_val
            
            if node is None:
                return "error"
            if node.value > max_val:
              max_val=node.value

            max(node.left)
            max(node.right)
        max(self.root)
        return max_val   
    
```


## Verification
```
def max_value(self):                                  Input
                                                        5
                                              8               9
                                       10 
              if not self.root:
            return "trss is empty "
        max_val=self.root.value...............max_val=5
        
        def max(node):
            nonlocal max_val
            
            if node is None:
                return "error"
            if node.value > max_val:     .......8>5               
                                                9>5
              max_val=node.value............10>8
                                      
            max(node.left).................max_val=10
            max(node.right)
        max(self.root)
        return max_val               ...output =10
    

   
```