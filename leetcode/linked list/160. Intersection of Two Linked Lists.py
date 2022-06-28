# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:


# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.


# P: can two linkedlist be none?
# are node value all positive integers?

# R: Can you please explain what do you want intersection? 
# first intersection node? 
# all intersection list?

# Persudo Code:
# 每步操作需要同时更新指针 pA 和 pB。
# 如果指针 pA 不为空，则将指针 pA 移到下一个节点；如果指针 pB 不为空，则将指针 pB 移到下一个节点。
# 如果指针 pA 为空，则将指针 pA 移到链表 headB 的头节点；如果指针 pB 为空，则将指针 pB 移到链表 headA 的头节点。
# 当指针 pA 和 pB 指向同一个节点或者都为空时，返回它们指向的节点或者 null。

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        pA = headA
        pB = headB
        
        while (pA != pB):
            if not pA: 
                pA = headB # 如果指针 pA 为空，则将指针 pA 移到链表 headB 的头节点
            else:
                pA = pA.next
            
            if not pB:
                pB = headA # 如果指针 pB 为空，则将指针 pB 移到链表 headA 的头节点。
            else:
                pB = pB.next
        return pA 
        