# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        E:
        P: 
        1. iterative through the ll and keep track of value != val in []
        2. loop throught again and replace the ll val with the value in []
        3. return new head
        """
        res = [] 
        newHead = head # keep track of newHead
        newLL = head #ptr to loop through new List
        
        while head != None:
            if head.val != val: 
                res.append(head.val) # add to result array
            head = head.next
        
        for i in range(len(res)):
            newLL.val = res[i] # replace the old ll with new value in result array
            if i != len(res) - 1: # if not hit the end of ll
                newLL = newLL.next # move the loop ptr one step later
            else:
                newLL.next = None
        return newHead if len(res) != 0 else None
        