234. Palindrome Linked List
Easy

7493

493

Add to List

Share
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

6.5回文链表
6.5.1算法要求
判断一个链表是否为回文链表
eg1:
输入：1-2
输出：false

eg2:
输入1-2-2-1
输出：true

进阶：
用o-n时间复杂度和o-1空间复杂度解决这个问题。

6.5.2解题思路
如果把回文链表当成图形来看，那么它是一个轴对称图形，和回文字符串类似。因此把回文链表的值放到一个链表中去，这个链表的*倒序*链表必定是和原链表相同的。以head=【1，2，2，1】为例。

6.5.3解题代码

1.反转链表的代码为：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None:
        	return True
        valList=[]

        while head:
        	valList.append(head.val)
        	head=head.next

        rList=valList[::-1]
        if rList==valList:
        	return True
        else: 
        	return False


2进阶(o-1?)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
