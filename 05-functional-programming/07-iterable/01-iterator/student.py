
class InclusiveRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return InclusiveRangeIterator(self.start, self.stop)



class InclusiveRangeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.stop:
            result = self.current
            self.current += 1
            return result

        else:
            raise StopIteration


for i in InclusiveRange(1, 5):
    print(i)

