21. Merge Two Sorted Lists
Easy

9886

956

Add to List

Share
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.


6.4合并两个有序链表
6.4.1算法要求
将两个有序链表合并为一个新的有序链表并且返回。新链表是通过拼接给定的两个列表的所有节点组成的。

示例：
输入：1-2-4，1-3-4
输出 1-1-2-3-4-4

6.4.2解题思路
合并两个有序链表，在逻辑上简单。比较11.val和12.val，谁比较小谁就是head.next,然后比较小的节点指向next，一直到两个链表结束。head应该指向哪个链表呢？先比较11.val和12.val？复杂。这里可以将head指向一个fakenode。head的next指向11和12比较小的节点。执行完毕后返回fakenode。next既可以了。以l1=[1,2,4],l2=[1,3,4]为例子。
比较l1.val和l2.val，l1.val比较小，将head。next指向比较小的那个节点l1.head往后移动一位。head。next=l1。l1的指针后移一位。l1=l1.next。如图6-17.比较l1。val和l2.val，明显l2.val比较小，将head。next指向l2，head。next=l2.l2的指针往后移动。继续下一轮比较
当两个链表都比较完毕时，fake链表整合了两条有序列表，返回fake。next即可。head=fake。next

6.4.3解题代码
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None: #两个链表都是空
        	return None
        fakeNode=ListNode(0)
        head=fakeNode

        while list1!=None or list2!=None: #两条链表遍历完毕
        	if list1==None: #l1遍历完毕
        		head.next=list2
        		list2=list2.next
        		head=head.next
        	elif list2==None: #l2遍历完毕
        		head.next=list1
        		list1=list1.next
        		head=head.next
        	else: #都没遍历完毕
        		if list1.val<=list2.val:
        			head.next=list1
        			list1=list1.next
        			head=head.next
        		else:
        			head.next=list2
        			list2=list2.next
        			head=head.next
        return fakeNode.next
