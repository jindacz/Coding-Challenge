from randomList import randomList
import timeit

iList=randomList(20)
def selectionSort(iList):
	if len(iList)<=1:
		return iList
	for i in range(0,len(iList)-1):
		if iList[i]!=min(iList[i:]) #使用min函数找到剩余数列中最小的那个数
			minIndex=iList.index(min(iList[i:])) #minIndex是最小数的下表
			iList[i],iList[minIndex]=iList[minIndex],iList[i]
		#print("第%d轮排序结果："%(i+1),end="")
		#print(iList)
	return iList

if __name__=="__main__":
	print(iList)
	print(selectionSort(iList))
	print(timeit.timeit("selectionSort(iList)","from __main__ import selectionSort,iList",number=100)