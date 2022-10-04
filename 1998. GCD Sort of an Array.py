class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        new = sorted(nums)
        fa = Counter()

        def find(x):
            if fa[x] == x:
                return x
            fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            if not fa[x]:
                fa[x] = x
            if not fa[y]:
                fa[y] = y
            fa1 = find(x)
            fa2 = find(y)
            if fa1 != fa2:
                fa[fa1] = fa2

        for val in nums:
            for i in range(2, int(val ** 0.5) + 1):
                if val % i == 0:
                    union(val, i)
                    union(val, val // i)

        for i in range(len(nums)):
            if nums[i] == new[i]:
                continue
            if find(nums[i]) != find(new[i]):
                return False

        return True