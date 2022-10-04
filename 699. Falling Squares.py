class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        def build(begin, end):
            if begin == end:
                return tree(begin, end, 0)
            mid = (begin + end) // 2
            return tree(begin, end, 0, build(begin, mid), build(mid + 1, end))

        def update(node, begin, end, val):
            if node.begin == begin and node.end == end:
                node.max1 = val
                node.tag = True
                return
            spread(node)
            mid = (node.begin + node.end) // 2
            if end <= mid:
                update(node.l, begin, end, val)
            elif begin > mid:
                update(node.r, begin, end, val)
            else:
                update(node.l, begin, mid, val)
                update(node.r, mid + 1, end, val)
            node.max1 = max(node.l.max1, node.r.max1)

        def querry(node, begin, end):
            if node.begin == begin and node.end == end:
                return node.max1
            spread(node)
            mid = (node.begin + node.end) // 2
            if end <= mid:
                return querry(node.l, begin, end)
            elif begin > mid:
                return querry(node.r, begin, end)
            else:
                return max(querry(node.l, begin, mid), querry(node.r, mid + 1, end))

        def spread(node):
            if not node.tag:
                return
            node.tag = False
            if node.l:
                node.l.max1 = node.max1
                node.l.tag = True
            if node.r:
                node.r.max1 = node.max1
                node.r.tag = True

        set1 = set()
        for x, y in positions:
            set1.add(x)
            set1.add(x + y)

        dic = {}
        for i, val in enumerate(sorted(list(set1))):
            dic[val] = i

        node = build(0, len(dic) - 1)

        res = []
        max1 = 0
        for x, y in positions:
            begin = dic[x]
            end = dic[x + y] - 1
            get = querry(node, begin, end)
            max1 = max(max1, get + y)
            res.append(max1)
            update(node, begin, end, get + y)
        return res


class tree:
    def __init__(self, begin, end, max1, l=None, r=None, tag=False):
        self.begin = begin
        self.end = end
        self.max1 = max1
        self.l = l
        self.r = r
        self.tag = tag