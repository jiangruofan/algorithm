class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.heap = []

    def push(self, val: int) -> None:
        if self.heap and self.heap[0] >= len(self.stack):
            self.heap = []
        if not self.heap:
            self.stack.append([val])
            if self.capacity > 1:
                self.heap.append(len(self.stack) - 1)
        else:
            self.stack[self.heap[0]].append(val)
            if len(self.stack[self.heap[0]]) == self.capacity:
                heappop(self.heap)

    def pop(self) -> int:
        while self.stack and not self.stack[-1]:
            self.stack.pop()
        if not self.stack:
            return -1
        res = self.stack[-1].pop()
        if len(self.stack[-1]) == self.capacity - 1:
            heappush(self.heap, len(self.stack) - 1)
        return res

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stack) or not self.stack[index]:
            return -1
        res = self.stack[index][-1]
        if len(self.stack[index]) == self.capacity:
            heappush(self.heap, index)
        self.stack[index].pop()
        return res

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)