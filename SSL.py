# Singly Linked Lists

# lists and dictionaries

# Time and Space Complexity
# How fast does it run, and how much space/memory does it use?
# Big O Notation

# Node
# Pointer = Variable

# classes allow us to create new data structures

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def add_to_back(self, val):
        new_node = Node(val)
        # if head of list is empty, set head to new node
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self
    
    def print_vals(self):
        runner = self.head
        while runner.next:
            print(runner.val)
            runner = runner.next
        print(runner.val)
        return self

    
sll1 = SLL()
sll1.add_to_back(10).add_to_back(5).add_to_back(9).add_to_back(13).add_to_back(6)
sll1.print_vals()


        
        
        
        









# node1 = Node(10)
# node1.next = Node(5)
# print(node1.val)
# print(node1.next.val)






