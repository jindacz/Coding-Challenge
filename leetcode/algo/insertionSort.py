from randomList import randomList
import timeit

iList=randomList(20)

def insertionSort(iList):
	if len(iList)<=1:
		return iList;
	for right in range(1,len(iList)):
		target=iList[right]
		for left in range(0,right):
			if target<=iList[left]:
				iList[left+1:right+1]=iList[left:right] #使用python切片敷值
				iList[left]=target
				break
		#print(“第%d轮排序结果:” %（right),end="")
		#print(iList)
	return iList

if __name__ == '__main__':
	print(iList)
	print(insertionSort(iList))
	print(timeit.timeit("insertionSort(iList)","from __main__ import insertionSort, iList",number=100))