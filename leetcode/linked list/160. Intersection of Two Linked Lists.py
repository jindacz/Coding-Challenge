# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:


# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.


# P: can two linkedlist be none?
# are node value all positive integers? determine by value or by address?

# R: Can you please explain what do you want intersection? 
# first intersection node? 
# I. all intersection list?
# II. tra

# Persudo Code:
# Multiple pass? n Dummy head? y Two pointer? 
# burte force? loop ever node in listB, for each in A check any of nodes is present in listB
# 1 maintain a set to store list nodes
# 2 traverse list A and insert the address(node object) of each node into the set
# 3 now traver list B and find the first node that is already present in the set
# 4 return the current node if it is found in the set
# 5 if lists do not intersect return None


def getIntersectionNode(headA, headB):
    b_nodes = set()
    temp_b = headB
    while temp_b:
        b_nodes.add(temp_b)
        temp_b = temp_b.next

    temp_a = headA
    while temp_a:
        if temp_a in b_nodes:
            return temp_a
        temp_a = temp_a.next
    return None 

# 每步操作需要同时更新指针 pA 和 pB。
# 如果指针 pA 不为空，则将指针 pA 移到下一个节点；如果指针 pB 不为空，则将指针 pB 移到下一个节点。
# 如果指针 pA 为空，则将指针 pA 移到链表 headB 的头节点；如果指针 pB 为空，则将指针 pB 移到链表 headA 的头节点。
# 当指针 pA 和 pB 指向同一个节点或者都为空时，返回它们指向的节点或者 null。
def getIntersectionNode2(headA, headB):
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


    