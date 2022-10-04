class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = [0]
        n = len(stoneValue)
        for val in stoneValue:
            prefix.append(prefix[-1] + val)

        dp = [[0 for _ in range(n)] for _ in range(n)]
        maxl = [[0 for _ in range(n)] for _ in range(n)]
        maxr = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            maxl[i][i] = maxr[i][i] = stoneValue[i]

        for i in range(2, n + 1):
            mid = 0
            for l in range(n - i + 1):
                r = l + i - 1
                while prefix[mid + 1] - prefix[l] < prefix[r + 1] - prefix[mid + 1]:
                    mid += 1
                if l < mid:
                    dp[l][r] = max(dp[l][r], maxl[l][mid - 1])
                if mid < r:
                    dp[l][r] = max(dp[l][r], maxr[mid + 1][r])
                if prefix[mid + 1] - prefix[l] == prefix[r + 1] - prefix[mid + 1]:
                    dp[l][r] = max(dp[l][r], maxl[l][mid], maxr[mid + 1][r])
                maxl[l][r] = max(maxl[l][r - 1], dp[l][r] + prefix[r + 1] - prefix[l])
                maxr[l][r] = max(maxr[l + 1][r], dp[l][r] + prefix[r + 1] - prefix[l])

        return dp[0][-1]
