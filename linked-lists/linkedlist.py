class LinkedList:
    def __init__(self, value):
        # Creates a new node with the value passed in
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
     
     # Printing the list   
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    
    def append(self, value):
        # Creates a new node with the value passed in
        new_node = Node(value)
        # If list is empty the head and tail will point to the new node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print("Value added")
        else:
            # If the list is not empty add the new node to the end of the list and shift the tail to point to the new node
            self.tail.next = new_node 
            self.tail = new_node
        self.length += 1
        return True 
    
    def pop(self):
       if self.length == 0:
           return None
       temp = self.head
       pre = self.head
       # Iterate through list until the tail is reached 
       while(temp.next):
           pre = temp 
           temp = temp.next 
       # Set the 2nd to last node as the tail node and set the tail.next as None 
       self.tail = pre
       self.tail.next = None 
       # Decrement the length of the list by 1
       self.length -= 1
       if self.length == 0:
           self.head = None
           self.tail = None 
       # Return the deleted node object 
       return temp






            
    
    
            
            
            
            
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
        
        
        
        
        
my_linked_list = LinkedList(4)




my_linked_list.append(2)


print(my_linked_list.head.value)

print(my_linked_list.tail.value)

print(my_linked_list.print_list())

print(my_linked_list.pop())


