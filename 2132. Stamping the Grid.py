class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        prefix =[[0] * (n + 1) for _ in range(m + 1)]
        dif = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i-1][j-1] == 0 and i + stampHeight - 1 < m + 1 and j + stampWidth - 1 < n + 1 and prefix[i+stampHeight-1][j+stampWidth-1] - prefix[i+stampHeight-1][j-1] - prefix[i-1][j+stampWidth-1] + prefix[i-1][j-1] == 0:
                    dif[i][j] += 1
                    dif[i+stampHeight][j] -= 1
                    dif[i][j+stampWidth] -= 1
                    dif[i+stampHeight][j+stampWidth] += 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dif[i][j] = dif[i][j] + dif[i-1][j] + dif[i][j-1] - dif[i-1][j-1]
                if dif[i][j] == 0 and grid[i-1][j-1] == 0:
                    return False

        return True