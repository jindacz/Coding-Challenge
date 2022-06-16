8.3数组洗牌
8.3.1算法要求
打乱一个没有重复元素的数组
e.g:
//以数字集合1，2，3初始化数组
int[] nums={1,2,3}
Solution solution=new Solution(nums);

//打乱数组【1，2，3】并返回结果。任何【1，2，3】的排列返回的概率应该相同。
solution.shuffle();

//重设数组到初始状态【1，2，3】
solution.reset();

//随即返回数组【1，2，3】打乱后的结果。
solution.shuffle();

8.3.2解题思路
题目reset函数只要将nums返回就行了。至于shuffle函数，意思就是将nums列表中的元素交换位置，类似于洗牌。以nums=【1，2，3】为例。

class Solution:

    def __init__(self, nums: List[int]):
    	self.nums=nums
        
    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
    	import random
    	sList=self.nums[:] #深复制，不影响原来的数组。 不能使用浅复制sList=self.nums，修改后会影响原数组
    	rList=[]

    	while sList:
    		val=random.choice(sList)
    		rList.append(val)
    		sList.remove(val)
    	return rList
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()