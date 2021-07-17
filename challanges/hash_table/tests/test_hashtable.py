
from challanges.hash_table.hash_table import  Hashtable



def test_hash_table():
    hashtable = Hashtable(9)
   

    #test for hash method
    assert hashtable.hash('leen') == 6


    # test  for one input
  
    hashtable.add('liyan', 9)
    hashtable.add('firas', 10)
    
    #test for contains method

    assert hashtable.contains('liyan') is True
    assert hashtable.contains('lyian') is False

    
    # test for multiple input

    hashtable.add('lili', 90)
    hashtable.add('lulu', 'sweety')

    
    assert hashtable.contains('lili') is True
    assert hashtable.contains('lulu') is True

    assert hashtable.contains('firas') is True
    assert hashtable.contains('narin') is False
    
     # test FOR can't add exist key

    assert hashtable.add('liyan',35) == None

     # test the values

    assert hashtable.get('liyan') == 9
    assert hashtable.get('lulu') == 'sweety'

    # test for not  exist key
    
    assert hashtable.get('lolo') == ' not found '

