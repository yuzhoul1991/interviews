import collections
import random

class UniqueRandomGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.used = set()
        nums = list(range(start, end))
        random.shuffle(nums)
        self.queue = collections.deque(nums)
        def generator():
            while self.queue:
                yield self.queue.pop()
                if len(self.queue) == 0:
                    nums = range(self.start, self.end)
                    self.queue = collections.deque(nums)
                    random.shuffle(self.queue)
                    self.used = set()
        self.itr = generator()

    def next(self):
        val = next(self.itr, None)
        self.used.add(val)
        return val

    def update(self, start, end):
        self.start = start
        self.end = end
        nums = [x for x in range(self.start, self.end) if x not in self.used]
        random.shuffle(nums)
        self.queue = collections.deque(nums)



if __name__ == '__main__':
    obj = UniqueRandomGenerator(0, 10)
    for i in range(20):
        if i == 2: obj.update(0, 5)
        print(obj.next())
