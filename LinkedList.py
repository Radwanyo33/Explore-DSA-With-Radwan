class Node: 
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node
    
    def Print(self):
        if self.head is None:
            print("The Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    #Start Create a LinkedList from Provided values
    def insert_values (self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    #End Create a LinkedList from Provided values   
    
    #Calculating the length of the LinkedList
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    #Length calculation ends
    
    # Remove an element at a given index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index for removing element")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next 
                break
            # Bypassing the next link by pointing the previous one with the node after the immediate next one.
            count += 1
            itr = itr.next
    #Insert an element at any given index
    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index for removing element")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next) #itr.next points the new inserted data location
                itr.next = node
                break
            count += 1
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ##ll.insert_at_beginning(5)
    #ll.insert_at_beginning(10)
    #ll.insert_at_end(89)
    ll.insert_values(["Banana","Orange","Apple","Grape","Mango"])
    ll.Print()
    print(f'The length of the LinkedList is {ll.get_length()}')
    ll.remove_at(2)
    #ll.remove_at(20)
    ll.Print()
    print(f'The length of the LinkedList is {ll.get_length()}')
    ll.insert_at(0,"Peach")
    ll.Print()
    print(f'The length of the LinkedList is {ll.get_length()}')
    ll.insert_at(3,"Coconut")
    ll.Print()
    print(f'The length of the LinkedList is {ll.get_length()}')