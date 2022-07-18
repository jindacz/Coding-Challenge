class Fib(object):
    def __init__(self):
        self.work = 0

    def results(self, n):
        return f"The {n}th Fibonacci number is {self.f(n)} and requires {self.work} computations" 
    
    def f(self, n):
        self.work += 1
        if n < 2:
            return n
        return self.f(n-1) + self.f(n-2)

print(Fib().results(6))

class FibMemo(Fib):
    def __init__(self):
        self.cache = {}
        self.work = 0

    def f(self, n):
        if n in self.cache:
            return self.cache[n]
        self.work += 1
        if n < 2:
            return n
        self.cache[n] = self.f(n-1) + self.f(n-2)
        return self.cache[n]
    
print(FibMemo().results(6))