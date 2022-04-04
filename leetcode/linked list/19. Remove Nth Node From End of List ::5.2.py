19. Remove Nth Node From End of List
Medium

8217

402

Add to List

Share
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

6.2删除链表的倒数第n个节点
6.2.1算法要求
给定一个链表，删除链表的倒数第n个节点，并且返回链表的头节点。

例子：给定一个链表1-2-3-4-5，n=2
删除倒数第二个节点后，链表变成1-2-3-5。

说明：给定的n保证有效
进阶：尝试使用一趟扫描实现

6.2.2解题思路
1.常规算法
按照题目的要求删除倒数第n个节点。那么按照常规的算法应该先统计总共有多少个节点，然后算出倒数第n个节点是正数第几个节点，然后删除这个节点，返回head，原理很简单，eg head=【1，2，3，4，5】，n=2.
常规算法简单，但是需要两次遍历。

2.进阶算法
进阶算法要求只使用一次扫描。定位到倒数第n个节点，使用一个指针，用一次扫描是做不到了，刚才的常规算法是一个指针，两次扫描彩定位了倒数第n个节点。想一次扫描，就只能使用双指针了。
两个指针相隔n个节点，双指针同时移动，相对距离一直不变。当right指针到达链表尾时，left.next就是倒数第n个节点，也就是被删除的节点

6.2.3解题代码
1.常规算法
删除链表倒数第n个节点的常规算法代码为：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer=head
        length=0
        while pointer: #统计链表长度
        	pointer=pointer.next
        	length+=1
        if length==1: #只有一个节点
        	return None

        pointer=head
        if n>=length: #删除第一个节点
        	head.val=head.next.val #删除头部
        	head.next=head.next.next
        else:
        	if n==1: #删除尾巴节点
        		for i in range(length-2):
        			pointer=pointer.next
        		pointer.next=None
        	else: #删除中间节点
        		for i in range(length-n-1):
        			pointer=pointer.next
        		pointer.next=pointer.next.next
        return head

需要考虑多种情况，比如只有一个节点，删除节点是头部，尾巴。

2.进阶算法
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    	if head.next==None: #如果头是空
    		return None

    	left=right=head
    	si=0 #计数器

    	while si<n:
    		si+=1
    		right=right.next #双指针right先走n步

    	if right==None: #如果先走n步的时候，right已经触碰到了底部，证明n>len(列表)
    		head=head.next #删除第一个节点
    		return head
 
    	while right.next!=None: #left和right同时移动直到right.next==none为止
    		left=left.next
    		right=right.next

    	if n==1: #删除最后一个节点
    		left.next=None

    	else: #删除中间的节点
    		left.next=left.next.next
    	return head
虽然使用了两个while，只扫描了一次，经过了一次遍历，时间复杂度是o-n


