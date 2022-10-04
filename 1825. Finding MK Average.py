from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.low = SortedList()
        self.mid = SortedList()
        self.high = SortedList()
        self.m = m
        self.sides = k
        self.mid1 = m - 2 * k
        self.deq = deque()
        self.sum1 = 0


    def addElement(self, num: int) -> None:
        self.deq.append(num)
        if not self.low or (num <= self.low[-1]):
            self.low.add(num)
        elif self.high and num >= self.high[0]:
            self.high.add(num)
        else:
            self.mid.add(num)
            self.sum1 += num
        if len(self.deq) > self.m:
            x = self.deq.popleft()
            if x <= self.low[-1]:
                self.low.remove(x)
            elif x >= self.high[0]:
                self.high.remove(x)
            else:
                self.mid.remove(x)
                self.sum1 -= x
        while len(self.low) < self.sides and self.mid:
            x = self.mid.pop(0)
            self.low.add(x)
            self.sum1 -= x
        while len(self.low) > self.sides:
            x = self.low.pop()
            self.mid.add(x)
            self.sum1 += x
        while len(self.high) < self.sides and self.mid:
            x = self.mid.pop()
            self.high.add(x)
            self.sum1 -= x
        while len(self.high) > self.sides:
            x = self.high.pop(0)
            self.mid.add(x)
            self.sum1 += x


    def calculateMKAverage(self) -> int:
        return -1 if len(self.mid) < self.mid1 else self.sum1 // self.mid1
