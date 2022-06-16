189. Rotate Array
Medium

7248

1137

Add to List

Share
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?


4.3旋转数组
给定一个数组，将数组中的元素向右移动k个位置，其中k大于0.

eg1:
输入【1，2，3，4，5，6，7】和k=3
输入【5，6，7，1，2，3，4】

4.3.2解题思路
至少要三种算法达到目的。仔细看一下要求，实际就是将列表尾部的元素添加到列表头部，而且按照给出的例子，添加到列表头部的这部分子列表还是原来的顺序

1.颠倒列表弹出添加元素
以示例中的数组nums=【1，2，3，4，5，6，7】为例。当k=1时，需要将数组尾部的元素7移动到nums0的位置。nums中其他的元素逐个往后变成7，1，2，3，4，5，6。
在python中把列表尾部的单个元素取出来很容易，使用list的函数pop（）就可以了。即使想取出列表头部的元素，也可以用pop（0）来取得，但想把一个元素插入到列表的头部就比较麻烦了。倒是把一个元素追加到列表尾部比较容易。使用list的内建函数append(n)就能做到。那么，将整个列表颠倒一下所有的问题解决。颠倒列表后，问题就变成了从列表头取出一个元素，然后把元素追加到尾巴。一个pop（0）和一个append（n）就解决了问题。按照题目问题，将k个元素追加到颠倒的列表尾巴后，将列表再颠倒一次就可以了。将列表整体颠倒有个方便的内奸函数reverse（）。
首先要做的就是先将列表颠倒一下。
按照题目要求，将k个元素逐个弹出追加到列表尾巴后，再次颠倒列表。
经过两次颠倒列表后得到了题目所要求的列表。

2.逐个移动元素
颠倒列表是一个取巧，现在来试一下笨办法。按照题目要求把尾巴插入头部。获取尾巴使用pop（）。插入稍微复杂点，使用切片赋值，将出了队列尾巴的所有整体往后移动。然后把取出的列表尾巴元素赋值给列表头。
经过k轮的取列表尾插入后，就得到了题目要求的列表。这个方法但是避免了颠倒。

3.整体移动元素块
按照示例中的最终结果，移动后的列表元素顺序并没有变化。直接一步到位地移动所有元素不是更简单吗？需要移动k个元素，直接把列表尾巴的k个元素整体移动到列表头部就好了。
这种方法可以一步到位，在数组很长，移动的元素比较多的情况下，理论上这种方法是最快的。

4.3.3解题代码
1.运行颠倒列表法
颠倒列表的rotate函数如下所示

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
        	return
        nums.reverse()
        k=k%len(nums) #避免大于k的长度
        while k>0:
        	temp=nums.pop(0)
        	nums.append(temp)
        	k-=1
        nums.reverse()
        return

2.逐个移动元素法
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
        	return
        k=k%len(nums)
        while k>0:
        	temp=nums[-1]
        	nums[1:]=nums[:-1]
        	nums[0]=temp
        	k-=1
        return

3.运行整体移动元素块
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
        	return
        k=k%len(nums)
        temp=nums[len(nums)-k:] #5,6,7
     	nums[k:]=nums[:len(nums)-k]
        nums[:k]=temp
        return