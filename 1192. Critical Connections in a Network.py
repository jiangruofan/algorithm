class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        levels = [-1 for _ in range(n)]
        dic = defaultdict(list)
        ans = []
        for x, y in connections:
            dic[x].append(y)
            dic[y].append(x)
        def dfs(node, fa, level):
            nonlocal levels
            if levels[node] != -1:
                return levels[node]
            res = level
            levels[node] = level
            for val in dic[node]:
                if val == fa:
                    continue
                get = dfs(val, node, level + 1)
                if get < res:
                    res = get
            if res > levels[fa]:
                ans.append([node, fa])
            return res
        dfs(0, -1, 1)
        return ans