import random

def randomList(n):
	#reutrn a length n list from 0 to 1000
	iList=[]
	for i in range(n):
		iList.append(random.randrange(1000))
	return iList

if __name__=="__main__":
	iList=randomList(10)
	print(iList)