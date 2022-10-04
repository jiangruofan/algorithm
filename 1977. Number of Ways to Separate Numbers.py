class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num == "0":
            return 0
        mod = 10 ** 9 + 7
        n = len(num)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        dp1 = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        for i in range(n, 0, -1):
            for j in range(n, i - 1, -1):
                if num[i - 1] == num[j - 1]:
                    dp1[i][j] = 1 + dp1[i + 1][j + 1]

        def check(x, y, leng):
            val = dp1[x][y]
            if val >= leng:
                return True
            else:
                return num[y - 1 + val] > num[x - 1 + val]

        dp[1][1] = 1
        dp[0][0] = 1

        for i in range(2, n + 1):
            for leng in range(1, i + 1):
                l = i - leng
                if num[l] == "0":
                    if l > 0:
                        dp[i][leng] = dp[i][leng - 1]
                    continue
                if l - leng < 0:
                    val = dp[l][l]
                else:
                    if check(l - leng + 1, l + 1, leng):
                        val = dp[l][leng]
                    else:
                        val = dp[l][leng - 1]
                dp[i][leng] = dp[i][leng - 1] + val
                dp[i][leng] %= mod

        return dp[-1][-1] % mod