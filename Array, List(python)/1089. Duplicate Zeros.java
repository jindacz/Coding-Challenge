//1089 Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

/*Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
*/

//非原数组修改
class Solution {
    public void duplicateZeros(int[] arr) {
    	ArrayList<Integer> arrList=new ArrayList<Integer>();
    		for(int i=0;i<arr.length;i++){
    			arrList.add(arr[i]);
    			if(arr[i]==0){
    				arrList.add(0);    		
    			}
    			arr[i]=arrList.get(i);
    		}
    }
}
//原数组修改 惊天神级算法
class Solution {
    public void duplicateZeros(int[] arr) {
    	for(int i=0;i<arr.length;i++){
    		if(arr[i]==0){
    			for(int j=arr.length-1;j>i;j--){
    				arr[j]=arr[j-1];
    			}
    			i++;
    		}
    	}
    }
}
