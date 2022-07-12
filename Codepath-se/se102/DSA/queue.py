class MyQueue(object):
    def __init__(self, k):
        self.queue = [0] * k
        self.front = -1
        self.rare = -1
        self.capacity = k
    
    def isEmpty(self):
        return self.front == -1
    
    def isFull(self): # circular view
        return (self.rare + 1) % capacity == front 

    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.front + 1
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        return True

    def front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def deQueue(self):
        if self.isEmpty():
            return False
        self.front == (self.front + 1) % self.capacity
        if (self.rare + 1) % self.capacity == self.front:
            self.front = self.rear = -1
       
        return True