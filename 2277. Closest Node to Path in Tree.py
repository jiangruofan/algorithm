class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dp = [[-1 for _ in range(15)] for _ in range(n)]
        deep = [0 for _ in range(n)]

        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)

        def dfs(node, parent, deep1):
            nonlocal deep, dp
            deep[node] = deep1
            dp[node][0] = parent
            for val in dic[node]:
                if val == parent:
                    continue
                dfs(val, node, deep1 + 1)

        dfs(0, -1, 0)

        for i in range(1, 15):
            for j in range(n):
                if dp[j][i - 1] != -1:
                    dp[j][i] = dp[dp[j][i - 1]][i - 1]

        def lca(x, y):
            if deep[x] < deep[y]:
                return lca(y, x)

            dis = deep[x] - deep[y]
            index = 0
            while dis:
                if dis & 1:
                    x = dp[x][index]
                dis >>= 1
                index += 1

            if x == y:
                return x

            for i in range(14, -1, -1):
                if dp[x][i] != dp[y][i]:
                    x = dp[x][i]
                    y = dp[y][i]

            return dp[x][0]

        res = []
        for x, y, target in query:
            res.append(max([lca(x, y), lca(x, target), lca(y, target)], key=lambda x: deep[x]))
        return res
