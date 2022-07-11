# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

class MovingAverage:
    
    def __init__(self, size):
        self.size = size
        self.queue = collections.deque()
        self.total = 0

    def next(self, val):
        if self.size < 1: # windows size must > 1
            return None

        self.queue.append(val)

        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()

        self.total += val
        print(self.total)
        print(len(self.queue))
        return self.total*1.0 / len(self.queue)

