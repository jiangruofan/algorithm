class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        root = trie()
        for val in nums:
            root.add(val)
        res = []
        for x, y in queries:
            res.append(root.cal(x, y))
        return res


class trie:

    def __init__(self):
        self.children = defaultdict(lambda: trie())
        self.num = -1
        self.min1 = float('inf')

    def add(self, val):
        index = 1 << 29
        cur = self
        for i in range(29, -1, -1):
            x = 1 if val & index else 0
            cur.min1 = min(cur.min1, val)
            cur = cur.children[x]
            index >>= 1
        cur.num = val
        cur.min1 = min(cur.min1, val)

    def cal(self, val, limit):
        cur = self
        if cur.min1 > limit:
            return -1
        index = 1 << 29
        for i in range(29, -1, -1):
            x = 0 if val & index else 1
            if cur.children[x].min1 > limit:
                x = 1 - x
            if cur.children[x].min1 > limit:
                return -1
            cur = cur.children[x]
            index >>= 1
        return cur.num ^ val
