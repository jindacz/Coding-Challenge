206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

方法一：iteration
题目解析
设置三个节点pre、cur、next

（1）每次查看cur节点是否为NULL，如果是，则结束循环，获得结果
（2）如果cur节点不是为NULL，则先设置临时变量next为cur的下一个节点
（3）让cur的下一个节点变成指向pre，而后pre移动cur，cur移动到next
（4）重复（1）（2）（3）

动画描述

https://github.com/MisterBooo/LeetCodeAnimation/blob/master/0206-Reverse-Linked-List/Animation/Animation.gif

class Solution {
    public ListNode reverseList(ListNode head) { 
    	ListNode prev=null;
    	ListNode curr=head;
    	while(curr!=null){ //循环条件
    		ListNode next=curr.next; //next往后
    		curr.next=prev; //核心操作，curr.next设置为前
    		prev=curr; //pre往后
    		curr=next; //curr往后
    	}
    	return prev; //current已经是null了，所以必须return prev
    }
}


//？？？？？？？？？？？？？？？？？？？？
方法2:递归
假设其余部分反转了，如何反转前面部分？
假设n(k+1)到n(m)已经反转，设置nk.next.next=nk，
需要注意的是n1的下一个节点指向null，否则可能会产生环

/**
     * 以链表1->2->3->4->5举例
     * @param head
     * @return
     */
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head==null||head.next==null){ //boundary case
        	return head;
        }
        ListNode newHead=reverseList(head.next);
           /*
            第一轮出栈，head为5，head.next为空，返回5
            第二轮出栈，head为4，head.next为5，执行head.next.next=head也就是5.next=4，
                      把当前节点的子节点的子节点指向当前节点
                      此时链表为1->2->3->4<->5，由于4与5互相指向，所以此处要断开4.next=null
                      此时链表为1->2->3->4<-5
                      返回节点5
            第三轮出栈，head为3，head.next为4，执行head.next.next=head也就是4.next=3，
                      此时链表为1->2->3<->4<-5，由于3与4互相指向，所以此处要断开3.next=null
                      此时链表为1->2->3<-4<-5
                      返回节点5
            第四轮出栈，head为2，head.next为3，执行head.next.next=head也就是3.next=2，
                      此时链表为1->2<->3<-4<-5，由于2与3互相指向，所以此处要断开2.next=null
                      此时链表为1->2<-3<-4<-5
                      返回节点5
            第五轮出栈，head为1，head.next为2，执行head.next.next=head也就是2.next=1，
                      此时链表为1<->2<-3<-4<-5，由于1与2互相指向，所以此处要断开1.next=null
                      此时链表为1<-2<-3<-4<-5
                      返回节点5
            出栈完成，最终头节点5->4->3-2->1
         */
        head.next.next=head;
        head.next=null;
        return newHead;
    }
}




