# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def mergeTwoLists(l1, l2):
	dummy = ListNode(0)
	curr = dummy 

	while l1 and l2:
		if l1.val < l2.val:
			curr.next = l1
			l1 = l1.next
		else:
			curr.next = l2
			l2 = l2.next
		curr = curr.next

	if not l1:
		curr.next = l1
	if not l2:
		curr.next = l2
	return dummy.next