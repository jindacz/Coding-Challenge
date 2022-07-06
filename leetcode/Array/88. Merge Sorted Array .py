8.排序和搜索设计问题
本章包含了leetcode中的两节：排序和搜索，设计问题。因为这两节的题型比较相近，题目比较少，合并。
8.1合并两个有序数组

8.1合并两个有序数组
给定两个整数数组nums1和nums2，将nums2合并到nums1，使得nums1成为一个有序数组。

说明：初始化nums1和nums2的元素数量为m和n
·假设nums1有足够的空间（大于m+n），来保存nums2中的元素

输入 nums1=【1，2，3，0，0，0】，m=3
nums2=【2，5，6】 n=3
输出：【1，2，2，3，5，6】

8.1.2
解题思路：
1.pythonic算法
这一道题简单地说就是一道排序题，将两个列表合并成一个列表后排序，给一个整数列表排序，以nums1=【1，2，3，0，0，0】，m=3
nums2=【2，5，6】 n=3为例。

所要做的仅仅是合并nums1和nums2，然后使用python的列表sort函数而已。

2.详细算法
pythonic取巧，虽然达到了目的，但是并不清楚是怎么做到的。现在来看详细的算法过程，没错还是排序。将两个列表合并，和插入排序很像。

与正规的插入排序相比，有序数组的插入不是从第二个数开始插入的，可以直接从第二个有序数组的组头开始插入，因为数组是有序的。

8.1.3解题代码

1.pythonic
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
        	nums1[m+i]=nums2[i]
        nums1.sort()
        return

2.详细代码
合并有序数组的详细代码：
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n]=nums2[:n]

        for right in range(m,m+n):
        	target=nums1[right]
        	for left in range(0, right):
        		if target<=nums1[left]:
        			nums1[left+1:right+1]=nums1[left:right] #使用python切片赋值
        			nums1[left]=target
        			break
        return
