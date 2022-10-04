class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0 , 0)]
        seen = set([(0, 0)])
        res = 0
        while heap:
            num, x, y = heappop(heap)
            res = max(res, num)
            if x == n - 1 and y == n - 1:
                return res
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= i < n and 0 <= j  < n and (i, j) not in seen:
                    seen.add((i, j))
                    heappush(heap, (grid[i][j], i, j))
