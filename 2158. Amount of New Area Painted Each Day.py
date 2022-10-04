class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        res = []
        tree = Counter()

        def update(begin, end, l, r, index):
            if tree[index] == r - l + 1:
                return 0
            if l >= begin and r <= end:
                get = r - l + 1 - tree[index]
                tree[index] = r - l + 1
                return get
            mid = (l + r) // 2
            if end <= mid:
                get = update(begin, end, l, mid, index * 2)
            elif begin > mid:
                get = update(begin, end, mid + 1, r, index * 2 + 1)
            else:
                x = update(mid + 1, end, mid + 1, r, index * 2 + 1)
                get = update(begin, mid, l, mid, index * 2) + x
            tree[index] = tree[index * 2] + tree[index * 2 + 1]
            return get

        for x, y in paint:
            res.append(update(x, y - 1, 0, 50000, 1))
        return res