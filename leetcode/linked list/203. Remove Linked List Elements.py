# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeElements(head, val):
    # 1. Create a “dummy” head to point to head (to ensure we always have a valid return node)
    dummy = ListNode(None)     
    dummy.next = head
    
    # 2. Create a new pointer curr pointing to “dummy” head
    curr = dummy

    while curr.next:
        if curr.next.val == val:
            # skip/remove the node
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next