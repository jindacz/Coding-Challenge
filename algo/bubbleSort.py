from randomList import randomList
import timeit

iList=randomList(20)

def bubbleSort(iList):
	if len(iList)<=1:
		return iList
	for i in range(1,len(iList)):
		for j in range(0,len(iList)-i):
			if iList[j]>=iList[j+1]: #compare相邻数字大小
				iList[j],iList[j+1]=iList[j+1],iList[j]
		#print("第 %d轮排序结果："%i,end="")
		#print(iList)
	return iList
if __name__=="__main__":
	print(iList)
	print(bubbleSort(iList))
	print(timeit.timeit("bubbleSort(iList)","from __main__ import bubbleSort,iList",number=100))
