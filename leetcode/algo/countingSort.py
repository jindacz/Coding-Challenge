from randomList import randomList
import timeit

iList=randomList(20)

def countingSort(iList):
	if len(iList)<=1:
		return iList
	iLen=len(iList)
	rList=[None]*iLen
	for i in range(iLen):
		small=0 #less than base
		same=0 #same as base
		for j in range(iLen):
			if iList[j]<iList[i]:
				small+=1
			elif iList[j]==iList[i]:
				same+=1
		for k in range(small,small+same):
			rList[k]=iList[i]
	return rList

if __name__ == '__main__':
	print(iList)
	print(countingSort(iList))
	print(timeit.timeit("countingSort(iList)","from __main__ import countingSort,iList",number=100)) 