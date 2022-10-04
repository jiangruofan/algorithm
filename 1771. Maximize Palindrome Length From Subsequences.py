class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        leng = len(s)
        leng1 = len(word1)
        dp = [[0 for _ in range(leng)] for _ in range(leng)]
        res = 0
        for i in range(leng-1, -1, -1):
            for j in range(i, leng):
                if i == j:
                    dp[i][j] = 1
                elif i + 1 == j:
                    dp[i][j] = 2 if s[i] == s[j] else 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]) if s[i] != s[j] else 2 + dp[i+1][j-1]
                if i < leng1 and j >= leng1 and s[i] == s[j]:
                    res = max(res, dp[i][j])
        return res