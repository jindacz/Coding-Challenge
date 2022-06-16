# 118

# 11.4帕斯卡三角形
# 11.4.1算法要求
# 给定一个非负整数numRows，生成帕斯卡三角形前numsRows行。

# 11.4.2
# 这道题可以看出subList【0】=subList【-1】=1.已知子列表首元素和尾元素的值，然后根据位置求和。

class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		ret=list()

		for i in range(numRows):
			row=list()
			for j in range(0,i+1):
				if j==0 or j==i:
					row.append(1)
				else:
					row.append(ret[i-1][j]+ret[i-1][j-1])
			ret.append(row)
		return ret