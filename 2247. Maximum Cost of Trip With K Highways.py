class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        dic = defaultdict(list)
        for x, y, cost in highways:
            dic[x].append((y, cost))
            dic[y].append((x, cost))

        @cache
        def dfs(node, visited):
            if visited.bit_count() == k + 1:
                return 0

            res = -float('inf')
            for next_node, cost in dic[node]:
                if visited & (1 << next_node) == 0:
                    res = max(res, dfs(next_node, visited | (1 << next_node)) + cost)

            return res

        ans = -1
        for i in range(n):
            ans = max(ans, dfs(i, 1 << i))
        return ans
