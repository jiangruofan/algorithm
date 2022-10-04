class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        fa = [i for i in range(n)]
        size = [1 for _ in range(n)]
        map1 = {}
        for i, val in enumerate(nums):
            map1[val] = i

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
            fa[fa1] = fa2
            size[fa2] += size[fa1]

        max1 = max(nums)
        for limit in range(2, max1 + 1):
            candidates = []
            for val in range(limit, max1 + 1, limit):
                if val in map1:
                    candidates.append(map1[val])

            for i in range(1, len(candidates)):
                union(candidates[i - 1], candidates[i])

        return max(size)