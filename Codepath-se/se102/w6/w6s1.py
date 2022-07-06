class MinStack:

    def __init__(self, l):
        self.min_stack = []
        self.stack = []
        for i in l:
            self.push(i)

    def push(self, i):
        self.stack.append(i)
        if not(self.min_stack) or i <= self.min_stack[-1]:
            self.min_stack.append(i)

    def pop(self):
        removed = self.stack.pop()
        if removed == self.min_stack[-1]:
            self.min_stack.pop()

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None


def main():
    s = MinStack([])
    print('Test 0:', s.get_min() == None)

    s = MinStack([1])
    print('Test 1:', s.get_min() == 1)

    s = MinStack([2, 1])
    print('Test 2:', s.get_min() == 1)

    s = MinStack([1, 2])
    print('Test 3:', s.get_min() == 1)

    s = MinStack([2, 3])
    print('Test 3:', s.get_min() == 2)

    s = MinStack([3, 2, 1])
    print('Test 4:', s.get_min() == 1)

    s = MinStack([1, 2, 3])
    print('Test 5:', s.get_min() == 1)

    s = MinStack([2, 1, 1])
    print('Test 6:', s.get_min() == 1)

    s = MinStack([2, 3, 1])
    s.pop()
    print('Test 7:', s.get_min() == 2)

    s = MinStack([2, 3, 1, 4])
    s.pop()
    print('Test 8:', s.get_min() == 1)


main()
