class BookMyShow:

    def __init__(self, n: int, m: int):
        self.m = m
        self.n = n
        self.root = self.build(0, n - 1, m)

    def gather(self, k: int, maxRow: int) -> List[int]:
        return self.findmax(self.root, maxRow, k)

    def scatter(self, k: int, maxRow: int) -> bool:
        return self.cal(self.root, maxRow, k)

    def build(self, begin, end, val):
        if begin == end:
            return node(val, val, begin, end)
        mid = (begin + end) // 2
        l = self.build(begin, mid, val)
        r = self.build(mid + 1, end, val)
        return node(l.sum1 + r.sum1, val, begin, end, l, r)

    def findmax(self, node, maxRow, val):
        if node.begin > maxRow or node.max1 < val:
            return []
        if node.begin == node.end:
            ans = self.m - node.sum1
            node.sum1 -= val
            node.max1 = node.sum1
            return [node.begin, ans]
        mid = (node.begin + node.end) // 2
        if node.l.max1 >= val:
            ans = self.findmax(node.l, maxRow, val)
        else:
            ans = self.findmax(node.r, maxRow, val)
        node.sum1 = node.l.sum1 + node.r.sum1
        node.max1 = max(node.l.max1, node.r.max1)
        return ans

    def cal(self, node, maxRow, val):
        if node.sum1 < val or node.begin > maxRow:
            return False

        if node.begin == node.end:
            node.sum1 -= val
            node.max1 = node.sum1
            return True

        if node.l.sum1 >= val:
            judge = self.cal(node.l, maxRow, val)
            node.sum1 = node.l.sum1 + node.r.sum1
            node.max1 = max(node.l.max1, node.r.max1)
        else:
            judge = self.cal(node.r, maxRow, val - node.l.sum1)
            if judge:
                node.l.sum1 = 0
                node.l.max1 = 0
                node.sum1 = node.l.sum1 + node.r.sum1
                node.max1 = max(node.l.max1, node.r.max1)
        return judge


class node:

    def __init__(self, sum1, max1, begin, end, l=None, r=None):
        self.sum1 = sum1
        self.max1 = max1
        self.begin = begin
        self.end = end
        self.l = l
        self.r = r

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)