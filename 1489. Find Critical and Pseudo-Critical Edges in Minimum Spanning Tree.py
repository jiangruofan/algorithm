class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        critical = []
        pseudo = []

        def cal(list1, skip):
            res = 0
            father = [i for i in range(n)]

            def find(x):
                if x == father[x]:
                    return x
                father[x] = find(father[x])
                return father[x]

            def union(x, y):
                fa1 = find(x)
                fa2 = find(y)
                if fa1 != fa2:
                    father[fa1] = fa2

            for i, (x, y, weight, _) in enumerate(list1):
                if i == skip:
                    continue
                if find(x) != find(y):
                    res += weight
                    union(x, y)

            for i in range(n):
                if find(i) != find(0):
                    return float('inf')

            return res

        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])
        mst = cal(edges, -1)
        for i in range(len(edges)):
            if cal(edges, i) > mst:
                critical.append(edges[i][3])
            else:
                edges = [edges[i][::]] + edges
                if cal(edges, -1) == mst:
                    pseudo.append(edges[i + 1][3])
                edges = edges[1:]

        return [critical, pseudo]
