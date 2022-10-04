class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        dic = defaultdict(list)
        matrix = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        entry = [0 for _ in range(n + 1)]
        for x, y in edges:
            matrix[x][y] = True
            matrix[y][x] = True
            entry[x] += 1
            entry[y] += 1
            if x < y:
                dic[x].append(y)
            else:
                dic[y].append(x)

        res = float('inf')
        for node in range(n):
            leng = len(dic[node])
            for i in range(leng - 1):
                for j in range(i + 1, leng):
                    if matrix[dic[node][i]][dic[node][j]]:
                        res = min(res, entry[node] + entry[dic[node][i]] + entry[dic[node][j]] - 6)

        return res if res != float('inf') else -1
