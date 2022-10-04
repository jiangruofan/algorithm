class Solution:
    def minCut(self, s: str) -> int:
        leng = len(s)
        dp = [float('inf')] * leng
        dp[0] = 0
        for i in range(1, leng):
            s1 = s[:i+1]
            if s1 == s1[::-1]:
                dp[i] = 0
                continue
            for j in range(i):
                s1 = s[j+1:i+1]
                if s1 == s1[::-1]:
                    dp[i] = min(dp[i], 1 + dp[j])
        return dp[-1]