class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def dfs(x, y):
            max1 = 0
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[x][y]:
                    max1 = max(max1, dfs(i, j))
            return 1 + max1
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res