class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        leng = len(strs)
        dp = [1 for _ in range(n)]
        res = 1
        for i in range(1, n):
            for j in range(i):
                judge = True
                for k in range(leng):
                    if strs[k][j] > strs[k][i]:
                        judge = False
                if judge:
                    dp[i] = max(dp[i], dp[j]+1)
                    res = max(res, dp[i])
        return n - res
