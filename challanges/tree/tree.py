#Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
import re
from typing import overload


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#Binary Tree
#Create a Binary Tree class
#Define a method for each of the depth first traversals:


class Tree:
    def __init__(self):
        self.root = None
        
        # as the top of stack
    def pre_order(self):

        """
        we start from the root => left => right
        """
        
        try:
            #inial value to the output
            output = ''

            if not self.root:
                return output

            #define a closer func that will use internally
            #Closure is a function object that remembers values in enclosing scopes 
            #even if they are not present in memory.
            def _traverse(node):
                #we use nonlocal becous the output not accessable
                nonlocal output

                output = output + str(node.value)
                #if we have value in left call the func recursively for root.left
                if node.left:
                    _traverse(node.left)
                #if we have value in righht call the func recursively for root.right
                if node.right:
                    _traverse(node.right)
                return output
                #call the clouser fun and return the output
            _traverse(self.root)
            return output
        except:
            return 'there is an error in pre_order method'

    def in_order(self):

        """
        we start from farthest node from left => reach the root => then right
        """
        

        try:
            #initial the output
            output=""
            if not self.root:
                return output
            #defin inner func
            def traverse(node):
                nonlocal output
                #add to right
                if node.left:
                    traverse(node.left)
                output+=str(node.value)
                if node.right:
                    traverse(node.right)
                return output
            #call iner fuc and return the output
            traverse(self.root)
            return output
        except:
            return 'there is an error in in_order method'
    def post_order(self):

        """
        we start from left =>right => root
        """
        try:
            output=""
            if not self.root:
                return output
            def traverse(node):
                nonlocal output
                if node.left:
                    traverse(node.left)
                    #add to right
                if node.right:
                    traverse(node.right)
                output+=str(node.value)
                return output
            traverse(self.root)
            return output
        except:
            "ther is an error in post_order method"

    #####code challange 16 ###### 

    def max_value(self):

        """
        this method will return the max value in numeric tree

        """
        # check if the tree is empty
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

#Create a Binary Search Tree class which is inherit from tree class we use super to customize the original class.

class BinarySearchTree(Tree):
    #right high value then parent then the root less value
    
    def __init__(self):
        super().__init__()

    def add(self,value)   :

        """
        should add value in correct location in binary 
        right highest value then the parent then left
        
        """
        output=""
        if not self.root:
            self.root=Node(value)
            return output
        def traverse(node):
            if value >= node.value:
                #value in right shi=ould be the highest
                if not node.right:
                    node.right = Node(value)
                    return output
                traverse(node.right)
            else:
                if not node.left:
                    node.left = Node(value)
                    return output
                traverse(node.left)
        traverse(self.root)
        return output
    def Contains(self,value):

        """
        return boolean indicating whether or not the value is in the tree at least once

        """
        if not self.root:
            return False

        output=False
        def check_in(node):
            nonlocal output
            if node.value == value:
                output=True
                return output
            if value > node.value:
                if not node.right:
                   return output
                check_in(node.right)
            else:
                if not node.left:
                   return output
                check_in(node.left)

        check_in(self.root)
        return output