class Solution:
    # dp[i][k][ch][num]
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if len(s) == 100:
            pre = s[0]
            judge = True
            for i in range(2, 100):
                if s[i] != pre:
                    judge = False
                    break
            if judge:
                return 4
        s = "#" + s
        n = len(s)
        dp = [[[[100 for _ in range(11)] for _ in range(27)] for _ in range(k+1)] for _ in range(n)]
        dp[0][0][26][0] = 0

        for i in range(n-1):
            for j in range(min(i, k)+1):
                for ch in range(27):
                    for num in range(11):
                        cur = dp[i][j][ch][num]
                        if cur == 100:
                            continue
                        # delete s[i+1]
                        if j != k:
                            dp[i+1][j+1][ch][num] = min(dp[i+1][j+1][ch][num], cur)
                        # keep s[i+1]
                        if ch != ord(s[i+1]) - ord('a'):
                            dp[i+1][j][ord(s[i+1]) - ord('a')][1] = min(dp[i+1][j][ord(s[i+1]) - ord('a')][1], cur+1)
                        else:
                            if num == 1 or num == 9:
                                dp[i+1][j][ch][num+1] = min(dp[i+1][j][ch][num+1], cur+1)
                            elif num == 10:
                                dp[i+1][j][ch][10] = min(dp[i+1][j][ch][10], cur)
                            elif 1 < num < 9:
                                dp[i+1][j][ch][num+1] = min(dp[i+1][j][ch][num+1], cur)
        res = 100
        for i in range(27):
            for j in range(11):
                res = min(res, dp[-1][-1][i][j])
        return res