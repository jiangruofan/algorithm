class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        fa = [i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]

        def find(x):
            if x == fa[x]:
                return x
            fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fa1 = find(x)
            fa2 = find(y)
            if fa1 == fa2:
                return
            if rank[fa1] < rank[fa2]:
                fa[fa1] = fa2
            elif rank[fa1] > rank[fa2]:
                fa[fa2] = fa1
            else:
                fa[fa1] = fa2
                rank[fa2] += 1

        for limit in range(threshold + 1, n + 1):
            for val in range(2 * limit, n + 1, limit):
                union(val - limit, val)

        res = []
        for x, y in queries:
            res.append(True if find(x) == find(y) else False)

        return res