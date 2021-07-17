
from challanges.hash_table.linkedlist import linkedlist

class  Hashtable:
    def __init__(self,size):
        self.size = size
        self.map = [None]*size

    def hash(self,key):
        
        """
        this method will
        Returns the Index in the collection for
        that key

        """
        #ASCII codes represent text in computers
        #initial value
        sum_of_ascci_code=0
        for charachter in key:
            assci_code_charachter=ord(charachter)
            #In Python, the ord() function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument.

            sum_of_ascci_code=sum_of_ascci_code+assci_code_charachter
        temp_value=sum_of_ascci_code * 19
        hash_key=temp_value % self.size
        return hash_key
        
    def add(self,key,value):

        """
        This method should hash the key,
        and add the key and value pair to the table.
        
        """
        #hash key
        hash_key=self.hash(key)
        if not self.map[hash_key]:
            self.map[hash_key]=linkedlist()
        self.map[hash_key].add((key,value))


    def contains(self,key):

        """
        Returns a boolean, indicating if the key
        exists in the table already

        """
        hash_key=self.hash(key)
        #not exists
        if self.map[hash_key] is None:
         return False

        else:
            temp=self.map[hash_key].value()
            for item in temp:
                #exists
                if item[0] == key:
                    return True
            return False        

    def get(self,key):

        """
        Returns a value associated with that key 
        in the table if exist

        """
        hash_key=self.hash(key)
        #not exists
        if self.map[hash_key] is None:
         return " not found "

        temp=self.map[hash_key].value()
        # loop and check then return value
        for item in temp:
            if item[0] == key:
                return item[1]
        
