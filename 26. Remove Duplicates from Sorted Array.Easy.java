/*26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.




*/

You've hopefully already done this question, back when we were looking at deleting items from an Array. In that case, your algorithm might have looked something like this.

//class Solution {
    public int removeDuplicates(int[] nums) {
    	// The initial length is simply the capacity.
        int length=nums.length;

         // Assume the last element is always unique.
        // Then for each element, delete it iff it is
        // the same as the one after it. Use our deletion
        // algorithm for deleting from any index.
        for(int i=length-2;i>=0;i--){
        	if(nums[i]!=nums[i+1]){
        		// Delete the element at index i, using our standard
                // deletion algorithm we learned.
                for(int j=i+1;j<length;j++){
                	nums[j-1]=nums[j];
                }
                length--;

        	}
        }
        return length;
    }
}

//暴力
//public int[] compyWithRemovedDuplicates(int[] nums){
	//check for edge cases
	if(nums==null||nums.length==0){
		return nums;
	}
	//count how many unique elements are in the Array.
	int uniqueNumbers=0;
	for(int i=0;i<nums.length;i++){
		if(i==0||nums[i]!=nums[i-1]){
			 // An element should be counted as unique if it's the first
      // element in the Array, or is different to the one before it.
			uniqueNumbers++;
		}
	}
	int[] result=new int[uniqueNumbers];
	// Write the unique elements into the result Array.

	int positionInResult=0;
	for(int i=0;i<nums.length;i++){
		// Same condition as in the previous loop. Except this time, we can write
    // each unique number into the result Array instead of just counting them.
		if(i==0||nums[i]!=nums[i-1]){
			result[positionInResult]=nums[i];
			positionInResult++;
		}
	}
	return result;
}

Did you notice the fatal flaw with this approach though? It's the wrong return type! We could copy the result array back into the input array... and then return the length... but this is not what the question wants us to do. We want to instead do the deletions with a space complexity of O(1)O(1) and a time complexity of O(N)O(N).

Have a go at this for yourself, and then we'll talk about the solution. Your algorithm must be in-place, and take no more than O(N)O(N) time. Good luck!


//简单解法

class Solution {
    public int removeDuplicates(int[] nums) {
    	int t=0;
    	for(int i=0;i<nums.length;i++){
    		if(i==0||nums[i]!=nums[i-1]){
    			nums[t]=nums[i];
    			t++;
    		}
    		return t;
    	}
    }
}

//双指针
class Solution {
    public int removeDuplicates(int[] nums) {
    	int n=nums.length;
    	if (n==0){
    		return 0;
    	}
    	int fast=1,slow=1;
    	while(fast<n){
    		if(nums[fast]!=nums[fast-1]){
    			nums[slow]=nums[fast];
    			++slow;
    		}
    		++fast;
    	}
    	return slow;
    }
}
