import re
from challanges.hash_table.hash_table import Hashtable


def repeated_word(input_str):

    if input_str == None :
        return None

        
    hash_table = Hashtable(1000)

    input = re.sub('\W+', ' ', input_str).lower().split()

    for one_word in input:

        if hash_table.contains(one_word):

            return one_word

        else:

            hash_table.add(one_word,one_word)