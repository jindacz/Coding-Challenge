# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:

class MyQueue(object):
    
    def __init__(self):
        self.main = []
        self.side = []

    def push(self, x): # enqueue function, add to last element
        return self.main.append(x)
        

    def pop(self): # dequeue function, remove the first element
        while self.main: # main = [1,2,3]
            self.side.append(self.main.pop()) # side = [3,2,1]
        ret = self.side.pop() # ret = 1, python default pop function remove the last element
        
        while self.side: # move the main back
            self.main.append(self.side.pop())
        return ret # return 1
            
        

    def peek(self): # get first
        return self.main[0]
        

    def empty(self): # check if is empty
        return not(self.main)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()