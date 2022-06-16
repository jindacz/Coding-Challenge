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


CH4 数组
4.1从排序数组中删除重复
在python中去掉列表重复元素的方法很多，比如用集合set的特性，使用包含in的特性去重

4.1.1算法要求
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度
不要使用额外的数组空间，你必须在原地修改输入数组并在o—1额外空间的条件下完成。

eg1:
给定nums=【1，1，2【 函数返回新的长度2，并且原数组nums的前两个元素被修改为1，2
说明，为什么返回数值是整数，输出的答案是数组呢？
请注意，输入数组是以引用方式传递的，意味着在函数中修改输入数组对调用者是可见的。想想内部操作如下。

//nums是引用传递的，不对实际参数做任何备份
int len=removeDuplicates(nums)

//在函数里修改输入数组对于调用者是可见的
//根据函数返回的长度打印出数组中长度范围的所有元素
for(int i=0;i<len;i++){
    print(nums[i]);
}

4.1.2解题思路
题中给出了一个已经排序过的列表，需要原地去重，然后返回新数组长度。要求不用额外空间。
nums已经是排序的列表，相同的元素必定是相邻的。要返回去重后元素的个数，要返回去重后元素的个数，借助python的集合概念，只需要len(set(nums))就足够了。要求新列表前面的元素为去重后的元素，那也不难，只需要将nums中相邻的元素比较即可，重复的相邻的两个元素，则将后面那个元素排到列表尾部就可以了。注意比较香玲两个元素不需要从头到尾，只需要比较到len（set（nums））就足够了。后面的列表nums【len（set（nums））：】必然都是重复的元素，不需要浪费时间比较了。设置【0，0，1，1，1，2，2，3，3，4】，首先要做的是去重，确定比较元素的边界，也就是len（set（sum））。
然后从列表头开始，一直到len（set（sum））为止，比较相邻元素。如果发现相邻的元素相等，就把后面部分整体向前移动一位。当前len（set（sum））=5，所以只需要从sum【0=比较到sum4就够了。sum【4】后面的元素sum【5:】必然都是重复的元素。首先开始比较sum【0】和sum【1】
用切片，可以把sum【2:】全体往前移动一位，把sum【1】移动到sum列表的尾部。全部移动到位后，新的sum列表为【0，1，1，1，2，2，3，3，4，0】。
sum【0】和sum【1】比较完毕。下一步是sum1和sum2.一次比较，一直到sum【len（set（sum））-1】，也就是sum4为止。

4.1.2解题思路
题中给出了一个已经排序过的列表，需要原地去重，然后返回新数组长度。要求不用额外空间。
nums已经是排序的列表，相同的元素必定是相邻的。要返回去重后元素的个数，要返回去重后元素的个数，借助python的集合概念，只需要len(set(nums))就足够了。要求新列表前面的元素为去重后的元素，那也不难，只需要将nums中相邻的元素比较即可，重复的相邻的两个元素，则将后面那个元素排到列表尾部就可以了。注意比较香玲两个元素不需要从头到尾，只需要比较到len（set（nums））就足够了。后面的列表nums【len（set（nums））：】必然都是重复的元素，不需要浪费时间比较了。设置【0，0，1，1，1，2，2，3，3，4】，首先要做的是去重，确定比较元素的边界，也就是len（set（sum））。
然后从列表头开始，一直到len（set（sum））为止，比较相邻元素。如果发现相邻的元素相等，就把后面部分整体向前移动一位。当前len（set（sum））=5，所以只需要从sum【0=比较到sum4就够了。sum【4】后面的元素sum【5:】必然都是重复的元素。首先开始比较sum【0】和sum【1】
用切片，可以把sum【2:】全体往前移动一位，把sum【1】移动到sum列表的尾部。全部移动到位后，新的sum列表为【0，1，1，1，2，2，3，3，4，0】。
sum【0】和sum【1】比较完毕。下一步是sum1和sum2.一次比较，一直到sum【len（set（sum））-1】，也就是sum4为止。

#does not work 边界case
#class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(set(nums))
        i=0
        while i<n-1:
        	if nums[i]==nums[i+1]:
        		temp=nums[i+1]
        		nums[i+1:len(nums)-1]=nums[i+2:]
        		nums[-1]=temp
        		continue
        	else:
        		i+=1
        return n



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        newTail=0

        for i in range(1,len(nums)):
        	if nums[i]!=nums[newTail]:
        		newTail+=1
        		nums[newTail]=nums[i]
        return newTail+1