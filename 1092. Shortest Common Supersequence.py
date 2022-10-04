class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str11 = str1
        str22 = str2
        str1 = list(str1)
        str2 = list(str2)
        path = defaultdict(tuple)
        m = len(str1)
        n = len(str2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
            path[(i, 0)] = (-1, -1, str11[:i])
        for i in range(n+1):
            dp[0][i] = i
            path[(0, i)] = (-1, -1, str22[:i])


        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    path[(i,j)] = (i-1, j-1, str1[i-1])
                else:
                    if dp[i-1][j] < dp[i][j-1]:
                        dp[i][j] = dp[i-1][j] + 1
                        path[(i, j)] = (i-1, j, str1[i-1])
                    else:
                        dp[i][j] = dp[i][j-1] + 1
                        path[(i, j)] = (i, j-1, str2[j-1])

        cur = (m, n)
        res = ""
        while path[cur]:
            x, y, s = path[cur]
            res = s + res
            cur = (x, y)
        return res