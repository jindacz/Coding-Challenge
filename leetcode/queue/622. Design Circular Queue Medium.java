622. Design Circular Queue
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

方法一：数组
思路

根据问题描述，该问题使用的数据结构应该是首尾相连的 环。

任何数据结构中都不存在环形结构，但是可以使用一维 数组 模拟，通过操作数组的索引构建一个 虚拟 的环。很多复杂数据结构都可以通过数组实现。

对于一个固定大小的数组，任何位置都可以是队首，只要知道队列长度，就可以根据下面公式计算出队尾位置：

\text{tailIndex} = (\text{headIndex} + \text{count} - 1) \mod \text{capacity}
tailIndex=(headIndex+count−1)modcapacity

其中 capacity 是数组长度，count 是队列长度，headIndex 和 tailIndex 分别是队首 head 和队尾 tail 索引。下图展示了使用数组实现循环的队列的例子。



算法

设计数据结构的关键是如何设计 属性，好的设计属性数量更少。

属性数量少说明属性之间冗余更低。

属性冗余度越低，操作逻辑越简单，发生错误的可能性更低。

属性数量少，使用的空间也少，操作性能更高。

*但是，也不建议使用最少的属性数量。*一定的冗余可以降低操作的时间复杂度，达到时间复杂度和空间复杂度的相对平衡。

根据以上原则，列举循环队列的每个属性，并解释其含义。

queue：一个固定大小的数组，用于保存循环队列的元素。

headIndex：一个整数，保存队首 head 的索引。

count：循环队列当前的长度，即循环队列中的元素数量。使用 hadIndex 和 count 可以计算出队尾元素的索引，因此不需要队尾属性。

capacity：循环队列的容量，即队列中最多可以容纳的元素数量。该属性不是必需的，因为队列容量可以通过数组属性得到，但是由于该属性经常使用，所以我们选择保留它。这样可以不用在 Python 中每次调用 len(queue) 中获取容量。但是在 Java 中通过 queue.length 获取容量更加高效。为了保持一致性，在两种方案中都保留该属性。


class MyCircularQueue {
    private int[] data;
    private int head;
    private int tail;
    private int size;
    //data init
    public MyCircularQueue(int k) {
        data=new int[k];
        head=-1;
        tail=-1;
        size=k;
    }
    //insert an element into the circular queue
    public boolean enQueue(int value) {
        if(isFull()==true){
            return false;
        }
        if(isEmpty()==true){
            head=0;
        }
        tail=(tail+1)%size;
        data[tail]=value;
        return true;

    }
    //delete an element from the circular queue
    public boolean deQueue() {
        if(isEmpty()==true){
            return false;
        }
        if(head==tail){
            head=-1;
            tail=-1;
            return true;
        }
        head=(head+1)%size;
        return true;

    }
    
    //get front item from the queue
    public int Front() {
        if(isEmpty()==true){
            return -1;
        }
        return data[head];
    }
    //get last item
    public int Rear() {
        if(isEmpty()==true){
            return -1;
        }
        return data[tail];

    }
    
    public boolean isEmpty() {
        return head==-1;

    }
    
    public boolean isFull() {
        return((tail+1)%size)==head;

    }
}
/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
