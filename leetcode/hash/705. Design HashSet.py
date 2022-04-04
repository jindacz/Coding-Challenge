705. Design HashSet

class MyHashSet:

    def __init__(self):
        

    def add(self, key: int) -> None:
        

    def remove(self, key: int) -> None:
        

    def contains(self, key: int) -> bool:
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



class MyHashSet:

    def __init__(self):
    	self.result=[]
        

    def add(self, key: int) -> None:
    	self.result.append(key)
        
    def remove(self, key: int) -> None:
    	if key in self.result:
    		self.result=list(set(self.result))
    		del self.result[self.result.index(key)]

    def contains(self, key: int) -> bool:
    	if key in self.result:
    		return True
    	else:
    		return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)