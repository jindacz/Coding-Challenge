461. Hamming Distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
    	xList=list(bin(x))[2::]
    	yList=list(bin(y))[2::]

    	if len(xList)<31:
    		xList=["0"]*(31-len(xList))+xList
    	if len(yList)<31:
        	yList=["0"]*(31-len(yList))+yList

    	n=0
    	for i in range(31):
    		if xList[i]!=yList[i]:
    			n+=1
    	return n