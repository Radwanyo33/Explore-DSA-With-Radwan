# Dictionary is a built in class of Python which automatically implements hash table
#This code shows the inner implementation of the Dictionary class of DSA HashMap / HashTable
# It provide O(1) time complexity on average cases

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char) #It returns the ASCII value of Character
        return h % self.MAX
     
    def __setitem__(self,key,value): #this function overrides the add function
        h = self.get_hash(key)
        self.arr[h] = value
        
    def __getitem__(self,key): #this function overrides the get function
        h = self.get_hash(key) #get the hash location
        return self.arr[h] #returns the value of particular hash location
        
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    """
    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
        
    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
        
    def remove(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    """    
    

if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 320
    t['march 1'] = 580
    t['dec 18'] = 400
    print(t['march 6'])
    print(t['march 1'])
    print(t['dec 18'])
    print("Before Deleting an element:")
    print(t.arr)
    print("After Deleting an element:")
    del t['march 1']
    print(t.arr)