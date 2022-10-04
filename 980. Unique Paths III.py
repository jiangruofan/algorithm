class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def code(x, y):
            return (1 << (x * n + y))

        graph = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    graph |= code(i, j)
                elif grid[i][j] == 1:
                    begin_x = i
                    begin_y = j
                elif grid[i][j] == 2:
                    end_x = i
                    end_y = j
                    graph |= code(i, j)

        @cache
        def dfs(x, y, graph):
            if x == end_x and y == end_y:
                if graph == 0:
                    return 1
                else:
                    return 0

            total = 0
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < m and 0 <= j < n and graph & code(i, j):
                    total += dfs(i, j, graph ^ code(i, j))
            return total

        return dfs(begin_x, begin_y, graph)