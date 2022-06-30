# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0) 
        dummy.next = head # set dummyHead
        temp = dummy

        while temp.next and temp.next.next: # [du, 1, 2, 3] -> [du, 2, 1, 3]
            first = temp.next # init/update mid ptr
            node2 = temp.next.next # init/update right ptr
            
            temp.next = node2 # du -> 2
            node1.next = node2.next # 1 -> 3
            node2.next = node1  # 2 -> 1

            temp = node1 # update p to next iteration, temp to 1
        return dummy.next


# t- o(n)
# s- o(1)
        