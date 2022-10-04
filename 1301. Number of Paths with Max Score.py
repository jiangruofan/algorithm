class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10 ** 9 + 7
        m, n = len(board), len(board[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        cnt = [[0 for _ in range(n)] for _ in range(m)]
        cnt[0][0] = 1
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    continue
                left = dp[i][j - 1] if j > 0 else 0
                top = dp[i - 1][j] if i > 0 else 0
                topLeft = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                max1 = max(left, top, topLeft)
                dp[i][j] = max1 + int(board[i][j] if board[i][j] not in "ES" else 0)
                cnt[i][j] += cnt[i][j - 1] if j > 0 and left == max1 else 0
                cnt[i][j] += cnt[i - 1][j] if i > 0 and top == max1 else 0
                cnt[i][j] += cnt[i - 1][j - 1] if i > 0 and j > 0 and topLeft == max1 else 0
        return [dp[-1][-1] % mod, cnt[-1][-1] % mod] if cnt[-1][-1] != 0 else [0, 0]

