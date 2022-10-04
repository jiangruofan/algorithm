class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        direction = ((-1, 0), (0, 1), (1, 0), (0, -1))
        dic = {0: "u", 1: 'r', 2: 'd', 3: "l"}
        distance = [[float('inf') for _ in range(n)] for _ in range(m)]
        heap = [(0, "", ball[0], ball[1])]

        def find(x, y, k):
            total = 0
            x += direction[k][0]
            y += direction[k][1]
            while 0 <= x < m and 0 <= y < n:
                if maze[x][y] == 1:
                    break
                total += 1
                if x == hole[0] and y == hole[1]:
                    break
                x += direction[k][0]
                y += direction[k][1]
            return total

        while heap:
            dis, path, x, y = heappop(heap)
            if x == hole[0] and y == hole[1]:
                return path
            if dis > distance[x][y]:
                continue
            distance[x][y] = dis
            for k in range(4):
                dis1 = find(x, y, k)
                x1 = x + direction[k][0] * dis1
                y1 = y + direction[k][1] * dis1

                if dis + dis1 < distance[x1][y1]:
                    heappush(heap, (dis + dis1, path + dic[k], x1, y1))
        return "impossible"

