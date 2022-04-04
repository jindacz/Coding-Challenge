237. Delete Node in a Linked List
Easy

3726

10757

Add to List

Share
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

 

Example 1:


Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:


Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 

Constraints:

The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node


6.1链表
算法中最常见的数据结构有链表和tree。相对而言链表简单，从简单的链表开始。
常见链表可以分为单向链表，双向链表，循环链表等。以最简单的单向链表为例，结构上可以分成两部分：数据域，指针域。其中数据域中存放的是链表的值，指针域存放的是一个指针。指向下一个链表，通过指针域，只需要找到头head，就可以遍历整个链表。

6.1删除链表中的节点
6.1.1算法要求
编写一个函数，删除某个链表中给定的节点，你将只被给定要求被删除的节点。
现在有链表head=【4，5，1，9】

输入head【4，5，1，9】
输出：【4，1，9】

·说明：链表至少包含2个节点
·链表所有节点值唯一
·给定节点为非末尾节点并且一定是有效节点
·不要返回任何结果

6.1.2解题思路
链表是数据结构中常用的数据类型。这一道题就是最基本的删除链表节点问题。以链表head=【4，5，1，9】为例，被删除node=5.
从物理上来说，node=5这个节点并没有被删除，只是重新赋值并且重新换了后面的节点，被删除的是node的下级节点。从效果上来看，node=5消失了。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next