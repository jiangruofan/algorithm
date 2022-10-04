class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        known = defaultdict(list)
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:
                    known[i].append(j)

        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)

        res = [-1 for _ in range(n)]

        def dfs(node, save, deep):
            nonlocal res
            depth = -1
            cnt = -1
            for val in known[nums[node]]:
                if val in save:
                    node1, depth1 = save[val]
                    if depth1 > depth:
                        depth = depth1
                        cnt = node1
            res[node] = cnt
            visited = set(x for x, _ in save.values())
            save[nums[node]] = (node, deep)
            for val in dic[node]:
                if val not in visited:
                    dfs(val, dict(save), deep + 1)

        dfs(0, {}, 0)

        return res