class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        n = len(equations)
        fa = {}
        val = {}

        def find(x):
            if fa[x] == x:
                return x
            old = fa[x]
            fa[x] = find(fa[x])
            val[x] *= val[old]
            return fa[x]

        def union(x, y, num):
            if x not in fa:
                fa[x] = x
                val[x] = 1
            if y not in fa:
                fa[y] = y
                val[y] = 1
            fa1 = find(x)
            fa2 = find(y)
            if fa1 != fa2:
                fa[fa2] = fa1
                val[fa2] = val[x] * num / val[y]
                return True
            else:
                return abs(val[y] / val[x] - num) < 1e-8

        for i in range(n):

            if not union(equations[i][0], equations[i][1], values[i]):
                return True

        return False
