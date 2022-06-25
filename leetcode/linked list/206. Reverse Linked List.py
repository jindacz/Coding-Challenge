# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	left=right=head #初始化

    	if head==None: #边界条件none
    		return None

    	if right.next==None: #边界条件：只有一个元素
    		return head

    	else:
    		right = right.next #right先行
    		left.next = None #原来的第一个变成现在的最后一个

    	while right != None: #开始循环
    		head = right #head第二个行动
    		right = right.next #right再往右一步
    		head.next = left #箭头转向
    		left = head #left往右边
    	return head