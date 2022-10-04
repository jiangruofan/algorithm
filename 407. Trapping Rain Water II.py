class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []
        m, n = len(heightMap), len(heightMap[0])
        seen = set()
        for i in range(n):
            heappush(heap, (heightMap[0][i], 0, i))
            heappush(heap, (heightMap[m - 1][i], m - 1, i))
            seen.add((0, i))
            seen.add((m - 1, i))
        for i in range(1, m - 1):
            heappush(heap, (heightMap[i][0], i, 0))
            heappush(heap, (heightMap[i][n - 1], i, n - 1))
            seen.add((i, 0))
            seen.add((i, n - 1))
        res = 0
        while heap:
            h, x, y = heappop(heap)
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if i >= 0 and i < m and j >= 0 and j < n and (i, j) not in seen:
                    if heightMap[i][j] < h:
                        res += h - heightMap[i][j]
                        heappush(heap, (h, i, j))
                    else:
                        heappush(heap, (heightMap[i][j], i, j))
                    seen.add((i, j))
        return res
