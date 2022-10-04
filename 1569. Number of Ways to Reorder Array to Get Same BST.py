class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        factorial = [1]
        for i in range(1, 1001):
            factorial.append(factorial[-1] * i % mod)

        @cache
        def fastPower(val, k):
            if k == 1:
                return val
            x = fastPower(val, k // 2)
            return x ** 2 % mod if k % 2 == 0 else (x ** 2) * val % mod

        def inverse(val):
            return fastPower(val, mod - 2)

        def dfs(nums):
            if len(nums) < 3:
                return 1
            l = [val for val in nums if val < nums[0]]
            r = [val for val in nums if val > nums[0]]
            ll = dfs(l)
            rr = dfs(r)
            return factorial[len(l) + len(r)] * inverse(factorial[len(l)]) * inverse(factorial[len(r)]) * ll * rr % mod

        return dfs(nums) - 1