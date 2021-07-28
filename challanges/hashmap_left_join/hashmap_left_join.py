from challanges.hash_table.hash_table import Hashtable
from challanges.hash_table.linkedlist import linkedlist

def left_join(hash_one,hash_two):
    # hash_one=Hashtable(1000)
    output_list=[]
    for value in hash_one.map:
        if value is not None:
            subarray=[]

            subarray.append(value.head.value[0])
            subarray.append(hash_one.get(value.head.value[0]))
            subarray.append(hash_two.get(value.head.value[0]))
            output_list.append(subarray)
           
    return output_list
