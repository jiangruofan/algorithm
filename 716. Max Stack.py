class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.dic1 = set()
        self.dic2 = set()
        self.index = 0

    def push(self, x: int) -> None:
        self.stack.append((x, self.index))
        heappush(self.heap, (-x, -self.index))
        self.index += 1

    def pop(self) -> int:
        self.cleanStack()
        x, y = self.stack.pop()
        self.dic2.add((x, y))
        return x

    def top(self) -> int:
        self.cleanStack()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        self.cleanHeap()
        return -self.heap[0][0]

    def popMax(self) -> int:
        self.cleanHeap()
        x, y = heappop(self.heap)
        self.dic1.add((-x, -y))
        return -x

    def cleanStack(self):
        while self.stack and self.stack[-1] in self.dic1:
            self.dic1.remove(self.stack.pop())

    def cleanHeap(self):
        while self.heap:
            x = -self.heap[0][0]
            y = -self.heap[0][1]
            if (x, y) in self.dic2:
                heappop(self.heap)
                self.dic2.remove((x, y))
            else:
                break

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()