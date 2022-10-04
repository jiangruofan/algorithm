class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        leng = len(s)
        dp = [[0] * leng for _ in range(leng)]
        for i in range(leng-1, -1, -1):
            for j in range(i, leng):
                if i == j:
                    dp[i][j] = 0
                elif j == i + 1:
                    dp[i][j] = 0 if s[i] == s[j] else 1
                else:
                    dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else min(dp[i+1][j], dp[i][j-1]) + 1
        return True if dp[0][-1] <= k else False