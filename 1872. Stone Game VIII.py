'''
dp[1] = 0
dp[2] = max  presum(n) - dp[1]
dp[3] = max presum(n) - dp[1], presum(n-1) - dp[2]
dp[4] = max presum(n) - dp[1], presum(n-1) - dp[2], presum(n-2) - dp[3]
'''

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        presum = [0]
        for val in stones:
            presum.append(presum[-1] + val)

        n = len(stones)
        dp = presum[-1]
        for i in range(3, n+1):
            dp = max(dp, presum[n+2-i] - dp)
        return dp

