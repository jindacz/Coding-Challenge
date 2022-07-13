#??? does not work
from randomList import randomList
from quickSort import quickSort
import random

iList=quickSort(randomList(20))
indexList=[[250,0],[500,0],[750,0],[1000,0]]

def divideBlock():
	global iList,indexList
	sortList=[]
	for key in indexList:
		subList=[i for i in iList if key[0]] #列表推导，小于key【0】的单独分块
		key[1]=len(subList)
		sortList+=subList
		iList=list(set(iList)-set(subList)) #过滤掉已经加入subList的元素
	iList=sortList
	print()
	return indexList

def blockSearch(iList, key):
    print("iList=%s" %str(iList))
    print("indexList=%s" %str(indexList))
    print("Find the number: %d" %key)
    left=0 #搜索数列的起点索引
    right=0 #搜索数列的终点索引
	
    for indexInfo in indexList:
        left+=right
        right+=indexInfo[1]
        if key<indexInfo[0]:
            break
    for i in range(left,right):
        if key==iList[i]:
            return i
    return -1

if __name__ == '__main__':
	print(iList)
	divideBlock()
	print(iList)
	keys=[random.choice(iList),random.randrange(min(iList),max(iList))]
	for key in keys:
		res=blockSearch(iList,key)
		if res>=0:
			print("%d is in the list, index is %d\n" %(key,res))
		else:
			print("%d is not in the list\n" %key)