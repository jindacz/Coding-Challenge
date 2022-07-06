# A single node of a singly linked list
class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    # insert method at the end of linked list
    def insert(self, data):
    	newNode = Node(data)
    	if(self.head):
    		current = self.head
    		while(current.next):
    			current = current.next
    		current.next = newNode
    	else:
    		self.head = newNode

# print method for linked list 
    def printLL(self):
    	current = self.head
    	while(current):
    		print(current.data)
    		current = current.next

# Singly Linked List with insertion and print method:
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()