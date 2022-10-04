class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        x = []
        y = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        x.sort()
        y.sort()
        x_mid = x[len(x) // 2]
        y_mid = y[len(y) // 2]
        res = 0
        for val in x:
            res += abs(val - x_mid)
        for val in y:
            res += abs(val - y_mid)
        return res