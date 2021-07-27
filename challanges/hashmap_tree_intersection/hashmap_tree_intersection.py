from challanges.hash_table.hash_table import Hashtable
from challanges.tree.tree import Node

def intersection(tree_one,tree_two):
    list=[]
    hash_table=Hashtable(1000)

    if tree_one.root==None and tree_two.root==None:
        return 'trees are empty'

    def _travers(node):

        nonlocal list
        nonlocal hash_table

        if hash_table.contains(str(node.value)):
            list=list+[node.value]

        else:
            hash_table.add(str(node.value),True)
        #add value in lest and right
        if node.left:
            _travers(node.left)
        if node.right:
            _travers(node.right)

    _travers(tree_one.root)
    _travers(tree_two.root)

    return list