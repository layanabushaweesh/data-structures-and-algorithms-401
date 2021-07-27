from challanges.hashmap_tree_intersection.hashmap_tree_intersection import intersection
from challanges.tree.tree import Tree
from challanges.tree.tree import Node



def test():
    tree1=Tree()

    tree1.root=Node(150)
    tree1.root.left=Node(100)
    tree1.root.right=Node(250)
    tree1.root.left.left=Node(75)
    tree1.root.left.right=Node(160)
    tree1.root.right.left=Node(200)
   

    tree2=Tree()
    tree2.root=Node(42)
    tree2.root.left=Node(100)
    tree2.root.right=Node(600)
    tree2.root.left.left=Node(15)
    tree2.root.left.right=Node(160)
    tree2.root.right.left=Node(200)
  
    

    actuall =intersection(tree1,tree2)
    excepted=[100, 160, 200]
    assert actuall == excepted

def test_2():

    tree1=Tree()

    tree1.root=Node(20)
    tree1.root.left=Node(15)
    tree1.root.right=Node(10)
    tree1.root.left.left=Node(30)
    tree1.root.left.right=Node(1)
  
   

    tree2=Tree()
    tree2.root=Node(60)
    tree2.root.left=Node(10)
    tree2.root.right=Node(30)
    tree2.root.left.left=Node(1)

    tree2.root.right.left=Node(2)
    actuall =intersection(tree1,tree2)
    excepted =[10, 1, 30]
    assert actuall == excepted
  
    
