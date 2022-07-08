/*346 Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

样例
Example 1:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
*/

solution 1: queue

public class MovingAverage {
	private Queue<Integer> que;
	private double sum=0;
	private int size;
    /*
    * @param size: An integer
    */public MovingAverage(int size) {
        // do intialization if necessary
    	que=new LinkedList<Integer>();
    	this.size=size;
    }

    /*
     * @param val: An integer
     * @return:  
     */
    public double next(int val) {
        // write your code here
        sum+=val;
        if(que.size()==size){
        	sum=sum-que.poll();
        }
        que.offer(val);
        return sum/que.size();
    }
}