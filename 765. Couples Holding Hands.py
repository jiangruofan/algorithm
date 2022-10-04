class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        fa = [i for i in range(n)]
        num = [1 for _ in range(n)]

        def find(node):
            if node == fa[node]:
                return node
            fa[node] = find(fa[node])
            return fa[node]

        def union(x, y):
            fa1 = find(x)
            fa2 = find(y)
            if fa1 != fa2:
                fa[fa1] = fa2
                num[fa2] += num[fa1]

        for i in range(0, n, 2):
            union(i, i + 1)
            union(row[i], row[i + 1])

        res = 0
        for i in range(n):
            fa1 = find(i)
            if num[fa1]:
                res += num[fa1] // 2 - 1
                num[fa1] = 0

        return res