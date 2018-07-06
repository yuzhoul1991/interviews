
class Modulo5Iterator:
    def __init__(self, itr):
        def generator(iterator):
            val = next(iterator, None)
            while val is not None:
                if val % 5 == 0:
                    yield val
                val = next(iterator, None)
            yield None
        self.itr = generator(itr)
        self.buffer = next(self.itr, None)

    def next(self):
        if self.hasNext():
            val = self.buffer
            self.buffer = next(self.itr, None)
            return val
        return None

    def hasNext(self):
        return self.buffer is not None


input = iter(range(100))
obj = Modulo5Iterator(input)
while obj.hasNext():
    print(obj.next())
