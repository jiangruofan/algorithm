class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        x = y = z = 0
        for val in nums:
            if val == 0:
                x = 2 * x + 1
            elif val == 1:
                y = 2 * y + x
            else:
                z = 2 * z + y
        return z % mod