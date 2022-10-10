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

class CountIntervals:

    def __init__(self):
        self.root = tree()
        

    def add(self, left: int, right: int) -> None:
        self.update(self.root, left, right, 1, 10 ** 9)


    def count(self) -> int:
        return self.root.total


    def update(self, node, left, right, l, r):
        if node.total == r - l + 1:
            return
        if left == l and right == r:
            node.total = r - l + 1
            return
        mid = (l + r) // 2
        if not node.lnode:
            node.lnode = tree()
        if not node.rnode:
            node.rnode = tree()
        if right <= mid:
            self.update(node.lnode, left, right, l, mid)
        elif left >= mid + 1:
            self.update(node.rnode, left, right, mid+1, r)
        else:
            self.update(node.lnode, left, mid, l, mid)
            self.update(node.rnode, mid + 1, right, mid+1, r)
        node.total = node.lnode.total + node.rnode.total


class tree:
    def __init__(self):
        self.total = 0
        self.lnode = None
        self.rnode = None

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
