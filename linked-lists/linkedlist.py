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
            print(f"Value added to the front of the list: {self.head.value}")

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


my_linked_list = LinkedList(4)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.append(8)
# # my_linked_list.append(4)
# # my_linked_list.pop_first()
# # my_linked_list.append(6)
# my_linked_list.prepend(9)
# my_linked_list.print_list()

node = my_linked_list.get(4)

print(node.value)