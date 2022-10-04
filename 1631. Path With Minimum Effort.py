class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        matrix = [[float('inf') for _ in range(n)] for _ in range(m)]
        matrix[0][0] = 0
        heap = [(0, 0, 0)]
        seen = set()
        while heap:
            max1, x, y = heappop(heap)
            if x == m - 1 and y == n - 1:
                return matrix[-1][-1]
            seen.add((x, y))
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if i >= 0 and i < m and j >= 0 and j < n and (i, j) not in seen:
                    new = max(max1, abs(heights[i][j] - heights[x][y]))
                    if new < matrix[i][j]:
                        matrix[i][j] = new
                        heappush(heap, (new, i, j))