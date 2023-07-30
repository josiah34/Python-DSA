"""


You are given a singly linked list implementation in Python that does not have a tail pointer (which will make this method simpler to implement).

You are tasked with implementing a method partition_list(self, x) that will take an integer x and partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.

You need to implement this method as a method of the LinkedList class. The method should take an integer x as input. If the linked list is empty, the method should return None.









"""











class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self, x):
        if self.head is None:
            return None

        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head

        while current is not None:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current

            current = current.next

        prev1.next = dummy2.next
        prev2.next = None

        self.head = dummy1.next

        return self.head

    

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10
