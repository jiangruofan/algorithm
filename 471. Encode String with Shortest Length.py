class Solution:
    def encode(self, s: str) -> str:
        s1 = s
        s = list(s)
        n = len(s)
        dp = [["" for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = s[i]

        def cal(x, y):
            res = s1[x:y + 1]
            n = len(res)
            for i in range(1, n):
                if n % i != 0:
                    continue
                judge = False
                for j in range(x, y + 1, i):
                    if s1[j:j + i] != s1[x:x + i]:
                        judge = True
                        break
                if judge:
                    continue
                new = str(n // i) + '[' + dp[x][x + i - 1] + ']'
                if len(new) < len(res):
                    res = new
            return res

        for leng in range(2, n + 1):
            for i in range(n - leng + 1):
                j = i + leng - 1
                dp[i][j] = cal(i, j)
                for k in range(i, j):
                    if len(dp[i][k]) + len(dp[k + 1][j]) < len(dp[i][j]):
                        dp[i][j] = dp[i][k] + dp[k + 1][j]

        return dp[0][-1]