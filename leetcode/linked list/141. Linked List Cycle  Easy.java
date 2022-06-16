/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

/*

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
*/

Follow up: Can you solve it using O(1) (i.e. constant) memory?

方法一：哈希表
思路及算法

最容易想到的方法是遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过。

具体地，我们可以使用哈希表来存储所有已经访问过的节点。每次我们到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表，否则就将该节点加入哈希表中。重复这一过程，直到我们遍历完整个链表即可。


public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> seen=new HastSet<ListNode>();
        while(head!=null){
        	if(!seen.add(head)){
        		return true;
        	}
        	head=head.next;
        }
        return false;
    }
}

方法二：快慢指针
思路及算法

本方法需要读者对「Floyd 判圈算法」（又称龟兔赛跑算法）有所了解。

假想「乌龟」和「兔子」在链表上移动，「兔子」跑得快，「乌龟」跑得慢。当「乌龟」和「兔子」从链表上的同一个节点开始移动时，如果该链表中没有环，那么「兔子」将一直处于「乌龟」的前方；如果该链表中有环，那么「兔子」会先于「乌龟」进入环，并且一直在环内移动。等到「乌龟」进入环时，由于「兔子」的速度快，它一定会在某个时刻与乌龟相遇，即套了「乌龟」若干圈。

我们可以根据上述思路来解决本题。具体地，我们定义两个指针，一快一slow。慢指针每次只移动一步，而快指针每次移动两步。初始时，慢指针在位置 head，而快指针在位置 head.next。这样一来，如果在移动的过程中，slow指针反过来追上fast指针，就说明该链表为环形链表。否则快指针将到达链表尾部，该链表不为环形链表。
。

细节

为什么我们要规定初始时慢指针在位置 head，快指针在位置 head.next，而不是两个指针都在位置 head（即与「乌龟」和「兔子」中的叙述相同）？

观察下面的代码，我们使用的是 while 循环，循环条件先于循环体。由于循环条件一定是判断快慢指针是否重合，如果我们将两个指针初始都置于 head，那么 while 循环就不会执行。因此，我们可以假想一个在 head 之前的虚拟节点，慢指针从虚拟节点移动一步到达 head，快指针从虚拟节点移动两步到达 head.next，这样我们就可以使用 while 循环了。

当然，我们也可以使用 do-while 循环。此时，我们就可以把快慢指针的初始值都置为 head。

代码

public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head==null || head.next==null){ //boundary conditions
        	return false;
        }
        ListNode slow=head;
        ListNode fast=head.next;
        while(slow!=fast){
        	if(fast==null||fast.next==null){
        		return false;
        	}
        	slow=slow.next;
        	fast=fast.next.next;
        }
        return true;
    }
}

复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是链表中的节点数。

当链表中不存在环时，快指针将先于慢指针到达链表尾部，链表中每个节点至多被访问两次。

当链表中存在环时，每一轮移动后，快慢指针的距离将减小一。而初始距离为环的长度，因此至多移动 NN 轮。

空间复杂度：O(1)O(1)。我们只使用了两个指针的额外空间。




