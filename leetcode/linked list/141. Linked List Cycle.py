141. Linked List Cycle
Easy

6491

710

Add to List

Share
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?


6.6环形列表
6.6.1算法要求
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数pos来表示链表尾连接到链表中的位置。如果pos是-1，证明没有环

输入head=【3，2，0，-4】，pos=1
输出：true
解释 链表中有一个环，尾巴连接到第二个节点。

输入head=【1，2】，pos=0
输出：true
解释 链表中有一个环，尾巴连接到第一个节点。

head=【1】。pos=-1
输出：false
链表中没有环

进阶：使用o（1）内存解决此问题

6.6.2解题思路
如果一个链表中有环，使用链表指针指向下一节点（head=head。next）的方式就陷入了死循环。这个链是无穷尽的。可以试试双指针，与前面的题不同的是，这次不是使用left，right指针，而是使用slow，fast指针。以head=【3，2，0，-4】，pos=“-12s3”为例。通过简单几个步骤，就可以得到转换后的数字。
使用快慢指针，快指针每次向前移动2步，慢指针每次向前移动1步。如果两个指针最后都指向None，说明这个链表不是环形。如果快慢指针指向同一个节点，说明是环形的。因为只有在一个环内，fast才能追上slow，否则将继续向前移动。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        fast=head
        slow=head

        while fast:
            try:
                fast=fast.next.next
                slow=slow.next
            except:         #在非环形链表中fast会先达到链表尾巴，slow继续下一步时，fast指针只能抛出异常
                return False
            if fast==None or slow==None:
                return False
            if fast==slow: #比较指针指向的节点，而不是节点的值。因为链表中可能有相同值
                return True
        