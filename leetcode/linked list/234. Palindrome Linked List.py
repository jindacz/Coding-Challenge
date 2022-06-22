# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1 reach the end of linkedlist by recursion
# 2 compare if the last node is same as the first nodes
# 3 second previous node has the same value as the second node
# 4 use stack and pointer
def isPalindrome(self, head):





# o(n) space

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
        