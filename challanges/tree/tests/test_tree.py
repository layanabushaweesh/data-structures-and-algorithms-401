import pytest

from challanges.tree.tree import Tree, Node ,BinarySearchTree



def test_pre_order_empty_tree():
    tree = Tree()
    assert tree.pre_order() == ''

def test_pre_order(prepared_tree):
    assert prepared_tree.pre_order() == 'liany'

def test_in_order(prepared_tree):
    assert prepared_tree.in_order() == 'ainly'


def test_post_order(prepared_tree):
    assert prepared_tree.post_order() == 'aniyl'



def test_Binary_Search_Tree_contain(binery):
    
    assert binery.Contains(2) == True
    assert binery.Contains(20) == False

def test_Binary_Search_Tree_add(binery):
    assert binery.pre_order() == '1234567'
    assert binery.post_order() == '7654321'
  



###code challange 16 ####

def test_max_value_1():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(10)
    tree.add(15)

    assert tree.max_value() == 15

def test_max_value_2():
    tree = BinarySearchTree()
    tree.add(20)
    tree.add(25)
    tree.add(30)

    assert tree.max_value() == 30



@pytest.fixture
def prepared_tree():
    tree = Tree()
    tree.root = Node('l')
    tree.root.left = Node('i')
    tree.root.right = Node('y')
    tree.root.left.left = Node('a')
    tree.root.left.right = Node('n')
    return tree

@pytest.fixture
def binery():
    new_one = BinarySearchTree()
    new_one.add(1)
    new_one.add(2)
    new_one.add(3)
    new_one.add(4)
    new_one.add(5)
    new_one.add(6)
    new_one.add(7)
  
  
  
    return new_one