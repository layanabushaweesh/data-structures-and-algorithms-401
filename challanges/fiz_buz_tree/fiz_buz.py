
class Node():
    def __init__(self,value):
        self.value=value
        # define list to put value of tree in it and loop in it
        self.list=[]

class k_ary_tree():
    def __init__(self):
        self.root=Node


def fizz_buzz_tree(k_ary_tree):
    def _fizz_buzz_tree(node):
        if node.list:
            #loop in list and check values
            for value in range(len(node.list)):
                _fizz_buzz_tree(node.list[value])
                if node.list[value].value % 5 == 0 and node.list[value].value %3 ==0 :
                    node.list[value].value = "FizzBuzz"

                
                elif node.list[value].value %3 ==0:
                    node.list[value].value = "Fizz"
                
                elif node.list[value].value %5 ==0:
                    node.list[value].value = "Buzz"
                else:
                 node.list[value].value = str(node.list[value].value)
    # check value for the root
    _fizz_buzz_tree(k_ary_tree.root)
    if k_ary_tree.root.value % 5 == 0 and k_ary_tree.root.value % 3 == 0:
         k_ary_tree.root.value == "FizzBuzz"
    elif k_ary_tree.root.value % 3 == 0:
         k_ary_tree.root.value = "Fizz"
    elif k_ary_tree.root.value %5 ==0:
         k_ary_tree.root.value ="Buzz"
    else:
        k_ary_tree.root.value = str(k_ary_tree.root.value)

    return k_ary_tree


