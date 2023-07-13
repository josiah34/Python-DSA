class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
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
        while temp.next:
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

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            # Set the
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return self.head

    def pop_first(self):
        # Checking for an empty list
        if self.head == None:
            return None
        # Checking for a list with only one value
        if self.head.next == None:
            self.head = None
            self.tail = None
            self.length = 0
            return True
        # List of size greater than 1
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1

    def get(self, index):
        # Give an error message if the index is greater than the length of the list or less than 0
        if index >= self.length or index < 0:
            print("Invalid index")
        else:
            temp = self.head
            # For loop iterates through list until the index is reached and then sets the temp node to the node at the index
            for _ in range(index):
                temp = temp.next
            # Print the value of the node at the index
            return temp

    def set(self, index, value):
        # Grab the node object at the index
        temp = self.get(index)
        # Change the value of the node object to the one passed into the method
        temp.value = value
        return temp
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return new_node
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next 
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp 
        
        
 
        
        
        
        
my_linked_list = LinkedList(4)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.insert(1,17)
# # my_linked_list.append(4)
# # my_linked_list.pop_first()
# # my_linked_list.append(6)
# my_linked_list.prepend(9)
# my_linked_list.print_list()

my_linked_list.set(0, 99)
my_linked_list.print_list()
print("-----------------------------")
print(my_linked_list.remove(4))
my_linked_list.print_list()
# node = my_linked_list.get(4)

# print(node.value)
