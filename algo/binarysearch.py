from randomList import randomList
from quickSort import quickSort
import random

iList=quickSort(randomList(20))

def binarySearch(iList,key):
	print("iList=%s" %str(iList))
	print("find the number:%d" %key)
	iLen=len(iList)
	left=0
	right=iLen-1

	while right-left>1:
		mid=(left+right)//2
		if key<iList[mid]:
			right=mid
		elif key>iList[mid]:
			left=mid
		else:
			return mid
		if key==iList[left]:
			return left
		elif key==iList[right]:
			return right
	return -1
    

if __name__ == '__main__':
	keys=[random.choice(iList),random.randrange(min(iList),max(iList))]
	for key in keys:
		res=binarySearch(iList,key)
		if res>=0:
			print("%d is in the list, index is %d\n" %(key,res))
		else:
			print("%d is not in the list\n" %key)
