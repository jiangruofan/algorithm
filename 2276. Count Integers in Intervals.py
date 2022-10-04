class CountIntervals:

    def __init__(self):
        self.tree = Counter()

    def add(self, left: int, right: int) -> None:
        self.update(left, right, 1, 10 ** 9, 1)

    def count(self) -> int:
        return self.tree[1]

    def update(self, begin, end, l, r, index):
        if self.tree[index] == r - l + 1:
            return
        if l >= begin and r <= end:
            self.tree[index] = r - l + 1
            return
        mid = (l + r) // 2
        if end <= mid:
            self.update(begin, end, l, mid, index * 2)
        elif begin > mid:
            self.update(begin, end, mid + 1, r, index * 2 + 1)
        else:
            self.update(begin, mid, l, mid, index * 2)
            self.update(mid + 1, end, mid + 1, r, index * 2 + 1)
        self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]
