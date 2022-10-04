class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 2
        for i in range(1, n):
            x = 0
            for j in range(i-1, -1, -1):
                if s[j] == s[i]:
                    x = dp[j-1] if j > 0 else 1
                    break
            dp[i] = 2 * dp[i-1] - x
            dp[i] %= mod
        return dp[-1] - 1