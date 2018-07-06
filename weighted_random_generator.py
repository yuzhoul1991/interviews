
import random
import collections

# GET O(n)
class WeightedRandomGenerator:
    def __init__(self):
        self.hsh = {}
        self.total_weight = 0

    def put(self, val, weight):
        if val in self.hsh:
            self.total_weight -= self.hsh[val]
        self.hsh[val] = weight
        if self.hsh[val] <= 0:
            del self.hsh[val]
        else:
            self.total_weight += weight

    def get(self):
        rnd = random.randrange(0, self.total_weight)
        for val, weight in self.hsh.items():
            if rnd < weight:
                return val
            rnd -= weight
        assert("Should never reach here")

# Get O(nlogn) using BIT to accelerate prefix sum
class WeightedRandomGenerator2:
    class BIT:
        def __init__(self, n):
            self._sums = [0] * (n+1)
        def update(self, i, delta):
            while i < len(self._sums):
                self._sums[i] += delta
                i += i & -i
        def prefix_sum(self, i):
            s = 0
            while i > 0:
                s += self._sums[i]
                i -= i & -i
            return s


    def __init__(self):
        self._tree = self.BIT(100)
        self._weights = {}
        self._orders = {}
        self._vals = []
        self.total_weight = 0

    def put(self, val, weight):
        if val in self._weights:
            self.total_weight -= self._weights[val]
            self._tree.update(self._orders[val], weight - self._weights[val])
        else:
            self._vals.append(val)
            self._orders[val] = len(self._vals)
            self._tree.update(self._orders[val], weight)

        self._weights[val] = weight
        self.total_weight += weight


    def get(self):
        rnd = random.randrange(0, self.total_weight)
        # do binary search on the prefix sum so GET is log(N) * log(N)
        left, right = 0, 100
        rnd_idx = -1
        while left < right:
            mid = left + (right - left)//2
            prefix_sum = self._tree.prefix_sum(mid+1)
            #print("mid ", mid, " prefix ", prefix_sum)
            if prefix_sum < rnd:
                left = mid + 1
            else:
                if mid == 0 or mid > 0 and self._tree.prefix_sum(mid) <= rnd:
                    rnd_idx = mid
                    break
                right = mid

        assert(0 <= rnd_idx < len(self._vals))
        return self._vals[rnd_idx]


if __name__ == '__main__':
    obj = WeightedRandomGenerator()
    obj.put(1, 20)
    obj.put(2, 60)
    obj.put(6, 10)
    obj.put(9, 10)
    obj.put(9, -10)


    total_itr = 10000
    counter = collections.Counter()
    for _ in range(total_itr):
        counter[obj.get()] += 1

    for k, v in counter.items():
        print("value {}, probability {}".format(k, v/total_itr))


