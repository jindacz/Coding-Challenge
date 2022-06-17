# Definition for singly-linked list.
class LinkedListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# PLAN:
# 1) Initialize two pointers (slow, fast) pointing at the head of the list
# 2) Iterate over the LinkedList while slow and fast pointers do not overlap
#     a) If fast's next (fast.next) or fast's next's next (fast.next.next) are Null, return False
#     b) Move slow 1 node forward
#     c) Move fast 2 nodes forward
# 3) Return True (while loop condition is broken, cycle found)

def hasCycle(head):
    if not head or not head.next:
        return False
    slow = head  # slow mover pointer
    fast = head.next  # fast mover pointer
    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        else:  # else just move slow one step and fast two steps at a time
            slow = slow.next
            fast = fast.next.next
    return False  # if fast pointer hits the end, no cycle!

node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node1.next = node2
node2.next = node3
node3.next = node1
print(hasCycle(node1))  # should be True

node1 = LinkedListNode(1)
print(hasCycle(node1))  # should be False

node1 = LinkedListNode(1)
node1.next = node1
print(hasCycle(node1))  # should be True