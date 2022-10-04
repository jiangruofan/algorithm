class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 +7
        res = 0
        nums.sort()

        first = 1
        second = 1 << (n-1)
        for i in range(n):
            res += nums[i] * first % mod
            res -= nums[i] * second % mod
            first <<= 1
            first %= mod
            second >>= 1
            res %= mod
        return res
