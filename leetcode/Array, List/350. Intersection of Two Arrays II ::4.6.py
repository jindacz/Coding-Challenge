350. Intersection of Two Arrays II
Easy

3656

622

Add to List

Share
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
///

4.6 两个数组的交集II
4.6.1 算法要求
给定两个数组，编写一个函数计算相交集。
eg1:
输入nums1=【1，2，2，1】，nums2=【2，2】
输出【2，2】
eg2:
输入nums1=【4，9，5】，nums2=【9，4，9，8，4】
输出【4，9】
说明：
输出结果每个元素出现的次数应该与元素在两个数组中出现的次数一致。
可以不考虑输出结果的顺序。

follow-up：
·如果给定的数组已经排好序？如何优化？
·如果nums1的大小比nums2小很多，哪种方法更优？
·如果nums2的元素存储在磁盘，内存有限，并且你不能一次加载所有的元素到内存中，你该怎么办？

4.6.2解题思路
如果只要求返回交集的元素就非常简单了，直接用python的list（set（nums1）&set（nums2））就搞定了；但题目还要求返回元素的个数，包括相同的交集元素。那就只能按步就规地一步一步算了。以 nums1=【1，2，2，1】，nums2=【4，1，2，3，1，2，3】为例。

1.排序求交集
首先要做的当然是排序，分别给nums1和nums2排序，然后在两个列表中按顺序各取出一个元素来比较.

比较的结果不相等，说明该元素不是交集。哪个列表取出的元素比较小，就取出这个列表中的下一个元素（类似于c语言中的指针往后一位），代替之前的元素，因为列表已经排序过了，下一个元素必定不小于前面的元素。
比较的两个元素相等时，说明这元素是交集元素，将这个元素加入到交集列表中，然后nums1和nums2同时取出下一个元素继续比较。

一直到某个列表所有的元素比较完毕为止。此时交集列表rList就是nums1和nums2列表的所有交集。

2.两列表长度相差大求交集
如果两个列表长度相差很大，就没有必要排序了，可以使用更加简单的办法来获取交集元素。不过首先要做的是确定哪个是长度短的列表。在函数未接受参数前，并不知道哪个列表的长度比较长，因此只有假设nums1的长度要远小于nums2的长度。即使实际情况不是如此，在函数中也要让运行情况如此。

然后遍历长度短的那个列表nums1.将元素取出后nums2中是否包含这个元素，如果不包含则比较nums2中的下一个元素（这里不需要排序，也无所谓元素的大小）。如果包含，则说明nums1取出的这个元素就是交集元素。在nums2中删除这个元素后，继续比较nums1列表的下一个元素。
一直到nums1所有元素都测试完毕为止。这种方法仅适用于nums1比nums2短很多的情况。

4.6.3
1.运行排序求交集
排序求交集的intersect函数的代码如下

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rList=[]
        nums1.sort()
        nums2.sort()
        p1=0 #point for nums1
        p2=0 #point for nums2

        while p1<len(nums1) and p2<len(nums2):
        	if nums1[p1]<nums2[p2]:
        		p1+=1
        	elif nums1[p1]==nums2[p2]:
        		rList.append(nums1[p1])
        		p1+=1
        		p2+=1
        	else:
        		p2+=1
        return rList

代码中第9，10行保证了nums1和nums2是有序的，然后进行比较来获取交集。

2.长短列表求交集法interset函数代码如下：
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rList=[]
        
        if len(nums1)>len(nums2):
        	nums1,nums2=nums2,nums1
        for n in nums1:
            if n in nums2:
                rList.append(n)
                nums2.remove(n)
        return rList

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums.append(nums1[i])
                nums2.remove(nums1[i])
        return(nums)

代码25，26保证了nums1是长度比较短的列表。在运行后发现排序求交集法的运行时间要短一点。这是因为两个列表比较短，长度相近，如果两个列表都比较长，长度悬殊，那么排序法花的时间可能就比较长了，毕竟排序也是需要时间的。

