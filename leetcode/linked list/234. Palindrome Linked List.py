# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        prev = head
        while prev != None:
            res.append(prev.val)
            prev = prev.next
        # print(res)
        # print(list(reversed(res)))
        return res == list(reversed(res))
        