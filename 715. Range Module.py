class RangeModule:

    def __init__(self):
        self.tree = Counter()

    def addRange(self, left: int, right: int) -> None:
        self.update(left, right - 1, 1, 10 ** 9, 1, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.find(left, right - 1, 1, 10 ** 9, 1) == 1

    def removeRange(self, left: int, right: int) -> None:
        self.update(left, right - 1, 1, 10 ** 9, 1, 2)

    def pushDown(self, index):
        if self.tree[index]:
            self.tree[index * 2] = self.tree[index]
            self.tree[index * 2 + 1] = self.tree[index]

    def update(self, begin, end, l, r, index, val):
        if self.tree[index] == val:
            return
        if l >= begin and r <= end:
            self.tree[index] = val
            return
        self.pushDown(index)
        mid = (l + r) // 2
        if end <= mid:
            self.update(begin, end, l, mid, index * 2, val)
        elif begin > mid:
            self.update(begin, end, mid + 1, r, index * 2 + 1, val)
        else:
            self.update(begin, mid, l, mid, index * 2, val)
            self.update(mid + 1, end, mid + 1, r, index * 2 + 1, val)
        self.tree[index] = self.tree[index * 2] & self.tree[index * 2 + 1]

    def find(self, begin, end, l, r, index):
        if l >= begin and r <= end:
            return self.tree[index]
        self.pushDown(index)
        mid = (l + r) // 2
        if end <= mid:
            return self.find(begin, end, l, mid, index * 2)
        elif begin > mid:
            return self.find(begin, end, mid + 1, r, index * 2 + 1)
        else:
            return self.find(begin, mid, l, mid, index * 2) & self.find(mid + 1, end, mid + 1, r, index * 2 + 1)

