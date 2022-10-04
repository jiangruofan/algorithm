class DistanceLimitedPathsExist:
    def find(self, node, limit):
        if node == self.fa[node] or limit <= self.limits[node]:
            return node
        return self.find(self.fa[node], limit)

    def __init__(self, n: int, edgeList: List[List[int]]):
        self.fa = [i for i in range(n)]
        self.limits = [-1 for _ in range(n)]
        self.deep = [1 for _ in range(n)]

        def union(x, y, cost):
            fa1 = self.find(x, float('inf'))
            fa2 = self.find(y, float('inf'))
            if fa1 == fa2:
                return
            if self.deep[fa1] > self.deep[fa2]:
                fa1, fa2 = fa2, fa1
            self.fa[fa1] = fa2
            if self.deep[fa1] == self.deep[fa2]:
                self.deep[fa2] += 1
            self.limits[fa1] = cost

        edgeList.sort(key=lambda x: x[2])
        for x, y, cost in edgeList:
            union(x, y, cost)

    def query(self, p: int, q: int, limit: int) -> bool:
        return self.find(p, limit) == self.find(q, limit)


