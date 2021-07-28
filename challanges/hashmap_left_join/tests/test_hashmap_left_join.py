from challanges.hash_table.hash_table import Hashtable
from challanges.hashmap_left_join.hashmap_left_join import left_join




def test_all_cases():
    hash_table_1 = Hashtable(1000)
    hash_table_1.add('fond', 'enamored')
    hash_table_1.add('wrath', 'anger')
    hash_table_1.add('diligent', 'employed')
    
   
    hash_table_2 = Hashtable(1000)
    hash_table_2.add('fond', 'averse')
    hash_table_2.add('wrath', 'delight')
    hash_table_2.add('diligent', 'idle')
    
   
    expected=left_join(hash_table_1,hash_table_2)
    actuall=  [
         
           ['fond',
            'enamored',
            'averse'],
           ['diligent',
            'employed',
            'idle'],
           ['wrath',
            'anger',
            'delight'],
                       ]
    assert expected == actuall
