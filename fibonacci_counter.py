class FibNumbers:
    def __init__(self, max_nums=None):
        self.first, self.second = 0, 1
        self.count = 0
        self.max_nums = max_nums

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_nums is not None and self.count >= self.max_nums:
            raise StopIteration
        fib = self.first
        self.first, self.second = self.second, self.first + self.second
        self.count += 1
        return fib

fib = FibNumbers(max_nums=15)
for num in fib:
    print(num)
