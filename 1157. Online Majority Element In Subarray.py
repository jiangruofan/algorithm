class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.dic = defaultdict(list)
        for i, val in enumerate(arr):
            self.dic[val].append(i)

        def build(begin, end):
            if begin == end:
                return Tree(begin, end, arr[begin], 1)

            mid = (begin + end) // 2
            left = build(begin, mid)
            right = build(mid + 1, end)

            cand = left.candidate if left.diff > right.diff else right.candidate
            dif = left.diff + right.diff if left.candidate == right.candidate else abs(left.diff - right.diff)

            return Tree(begin, end, cand, dif, left, right)

        self.node = build(0, len(arr) - 1)

    def query(self, left: int, right: int, threshold: int) -> int:
        def cal(node, begin, end):
            if node.begin == begin and node.end == end:
                return (node.candidate, node.diff)

            mid = (node.begin + node.end) // 2
            if end <= mid:
                return cal(node.l, begin, end)
            elif begin > mid:
                return cal(node.r, begin, end)
            x1, y1 = cal(node.l, begin, mid)
            x2, y2 = cal(node.r, mid + 1, end)
            c1 = x1 if y1 > y2 else x2
            d1 = y1 + y2 if x1 == x2 else abs(y1 - y2)
            return (c1, d1)

        candidate, _ = cal(self.node, left, right)
        l = bisect_left(self.dic[candidate], left)
        r = bisect_right(self.dic[candidate], right)
        x = r - l
        return candidate if x >= threshold else -1


class Tree:

    def __init__(self, begin, end, candidate, diff, l=None, r=None):
        self.begin = begin
        self.end = end
        self.l = l
        self.r = r
        self.candidate = candidate
        self.diff = diff
