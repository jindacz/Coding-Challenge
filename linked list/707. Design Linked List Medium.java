707. Design Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

面试要点
链表时一个包含零个或多个元素的数据结构。每个元素都包含一个值和到另一个元素的链接。根据链接数的不同，可以分为单链表，双链表和多重链表。

单链表是最简单的一种，它提供了在常数时间内的 addAtHead 操作和在线性时间内的 addAtTail 的操作。双链表是最常用的一种，因为它提供了在常数时间内的 addAtHead 和 addAtTail 操作，并且优化的插入和删除。

双链表在 Java 中的实现为 LinkedList，在 Python 中为 list。这些结构都比较常用，有两个要点：

哨兵节点：
哨兵节点在树和链表中被广泛用作伪头、伪尾等，通常不保存任何数据。

我们将使用伪头来简化我们简化插入和删除。在接下来的两种方法中应用此方法。

双链表的双向搜索：我们可以从头部或尾部进行搜索。
方法一：单链表
让我们从最简单的链表开始。


//注意negative index
class MyLinkedList {
	
	private class Node{
    	int val;
    	Node next;
    	public Node(int val){
    		this.val=val;
    	}
	}
	private int size;
	private Node head; //sentinel node as persudo-head

	/** Initialize your data structure here. */
    public MyLinkedList() {
   	

    }
    
    //get the value of the index-th node in the linked list, if index invalid,return -1
    public int get(int index) {
            if (index < 0 || index >= size) return -1;

            if (size == 1) {
                return head.val;
            }

            Node cur = head;
            for (int i = 0; i < index; i++) {
                cur = cur.next;
            }
            return cur.val;
        }

        /**
         * Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
         */
        public void addAtHead(int val) {
            if (head == null) {
                head = new Node(val);
            } else {
                Node n = new Node(val);
                n.next = head;
                head = n;
            }
            size++;
        }

        /**
         * Append a node of value val to the last element of the linked list.
         */
        public void addAtTail(int val) {
            if (head == null) {
                head = new Node(val);
            } else {
                Node cur = head;
                for (int i = 0; i < size - 1; i++) {
                    cur = cur.next;
                }
                cur.next = new Node(val);
            }
            size++;
        }

        /**
         * Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
         */
        public void addAtIndex(int index, int val) {
            if ( index > size) {
                return;
            }

            if (index <= 0) {
                addAtHead(val);
            } else if (index == size) {
                addAtTail(val);
            } else {
                Node cur = head;
                for (int i = 0; i < index - 1; i++) {
                    cur = cur.next;
                }
                Node node = new Node(val);
                node.next= cur.next;
                cur.next = node;

                size++;
            }
        }

        /**
         * Delete the index-th node in the linked list, if the index is valid.
         */
        public void deleteAtIndex(int index) {
            if (index < 0 || index >= size) {
                return;
            }
            size--;
            if (index == 0) {
                head = head.next;
                return;
            }

            Node cur = head;
            for (int i = 0; i < index - 1; i++) {
                cur = cur.next;
            }

            cur.next = cur.next.next;
        }


    }


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */


class MyLinkedList {
	

    public MyLinkedList() {

    }
    
    public int get(int index) {

    }
    
    public void addAtHead(int val) {

    }
    
    public void addAtTail(int val) {

    }
    
    public void addAtIndex(int index, int val) {

    }
    
    public void deleteAtIndex(int index) {

    }
}

