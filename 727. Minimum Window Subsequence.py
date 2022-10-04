class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        s1 = list(s1)
        s2 = list(s2)
        m, n = len(s1), len(s2)
        dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i-1][j] + 1
        min1 = float('inf')
        for i in range(m+1):
            if dp[i][n] < min1:
                min1 = dp[i][n]
                index = i
        if min1 == float('inf'):
            return ""
        else:
            return "".join(s1[index-min1:index])