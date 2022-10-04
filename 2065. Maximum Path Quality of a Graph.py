class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        dic = defaultdict(list)
        for x, y, time in edges:
            dic[x].append((y, time))
            dic[y].append((x, time))

        res = 0
        seen = set([0])

        def dfs(node, values1, times):
            nonlocal res
            if node == 0:
                res = max(res, values1)

            for node1, time in dic[node]:
                if times + time <= maxTime:
                    if node1 not in seen:
                        seen.add(node1)
                        dfs(node1, values1 + values[node1], times + time)
                        seen.remove(node1)
                    else:
                        dfs(node1, values1, times + time)

        dfs(0, values[0], 0)
        return res