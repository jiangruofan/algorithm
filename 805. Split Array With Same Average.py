class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        sum1 = sum(nums)
        if sum1 == 0:
            return True
        dp = [0 for _ in range(sum1)]
        dp[0] = 1

        for val in nums:
            for i in range(sum1 - 1, val - 1, -1):
                dp[i] |= dp[i - val] << 1
                if n * i % sum1 != 0:
                    continue
                x = n * i // sum1
                if x != 0 and x != n and dp[i] & (1 << x):
                    return True

        return False