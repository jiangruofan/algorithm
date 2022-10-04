class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        leng = len(grid)
        min1, minloc, min2 = 0, -1, 0
        for i in range(leng):
            x, y, z = float('inf'), -1, float('inf')
            for j in range(leng):
                cur = grid[i][j] + (min1 if j != minloc else min2)
                if cur < x:
                    x, y, z = cur, j, x
                elif cur < z:
                    z = cur
            min1, minloc, min2 = x, y, z
        return min1