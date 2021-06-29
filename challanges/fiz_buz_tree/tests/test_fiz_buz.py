from abc import ABC
from challanges.fiz_buz_tree.fiz_buz import Node
from challanges.fiz_buz_tree.fiz_buz import k_ary_tree
from challanges.fiz_buz_tree.fiz_buz import fizz_buzz_tree



def test_fiz_buzz_0():

    kAryTree = k_ary_tree()
    kAryTree.root=Node(0)
    kAryTree.root.list+=[Node(2)]
    kAryTree.root.list+=[Node(3)]
    kAryTree.root.list+=[Node(4)]
    fizz_buzz_tree(kAryTree)
    actuall =(kAryTree.root.list[1].value)
    excepted ='Fizz'
    assert actuall == excepted

def test_fiz_buzz_1():

    kAryTree = k_ary_tree()
    kAryTree.root=Node(0)
    kAryTree.root.list+=[Node(2)]
    kAryTree.root.list+=[Node(3)]
    kAryTree.root.list+=[Node(4)]
    fizz_buzz_tree(kAryTree)
    actuall =(kAryTree.root.list[2].value)
    excepted ='4'
    assert actuall == excepted

    
def test_fiz_buzz_2():

    kAryTree = k_ary_tree()
    kAryTree.root=Node(1)
    kAryTree.root.list+=[Node(2)]
    kAryTree.root.list+=[Node(15)]
   
    fizz_buzz_tree(kAryTree)
    actuall =(kAryTree.root.list[1].value)
    excepted ='FizzBuzz'
    assert actuall == excepted