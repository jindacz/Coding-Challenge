//485 Given a binary array nums, return the maximum number of consecutive 1's in the array.
为了得到数组中最大连续 11 的个数，需要遍历数组，并记录最大的连续 11 的个数和当前的连续 11 的个数。如果当前元素是 11，则将当前的连续 11 的个数加 11，否则，使用之前的连续 11 的个数更新最大的连续 11 的个数，并将当前的连续 11 的个数清零。

遍历数组结束之后，需要再次使用当前的连续 11 的个数更新最大的连续 11 的个数，因为数组的最后一个元素可能是 11，且最长连续 11 的子数组可能出现在数组的末尾，如果遍历数组结束之后不更新最大的连续 11 的个数，则会导致结果错误。

class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        // Hint: Initialise and declare a variable here to 
        // keep track of how many 1's you've seen in a row.
        int max=0;
        int count=0;
        for (int i = 0; i < nums.length; i++) {
            // Do something with element nums[i].
            if(nums[i]==1){count++;}
            else{
                max=Math.max(max,count);
                count=0;
            }

        }
            max=Math.max(max,count); //如果0结尾，正确；如果1结尾，需要更新max，因为
                                    //之前的case没有更新result
            return max;
    }
 }

复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组的长度。需要遍历数组一次。

空间复杂度：O(1)O(1)。

