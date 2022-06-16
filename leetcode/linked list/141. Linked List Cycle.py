# 141. Linked List Cycle
# Easy

# 6491

# 710

# Add to List

# Share
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

class LinkedListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
        # P 1. initilize two pointer(slow, fast) pointing at the head of the list()
        # 2. iterate over the LinkedList while slow and fast pointers do not overlap(while slow != fast)
        # a) if fast next's point or fast's next next are null -> False
        # 3. Return True (while loop condition is broken, cycle found)

        if head == None:
            return False
        fast = head.next  # fast pointer
        slow = head  # slow pointer

        # make sure its not a singly linkedlist
        while fast and fast.next:
            if slow == fast:
                return True  # cycle found
            else:  # just move slow one step at a time, and fast two steps at a time
                slow = slow.next  # one step
                fast = fast.next.next  # two steps
        return False

node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node1.next = node2
node2.next = node3
node3.next = node1  # cycle
print(hasCycle(node1))

node1 = LinkedListNode(1)
print(hasCycle(node1))  # should be False
node1 = LinkedListNode(1)
node1.next = node1
print(hasCycle(node1))  # should be True