class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        list1 = []
        for i in range(m):
            for j in range(n):
                list1.append((grid[i][j], i, j))
        list1.sort()
        maxR = [0 for _ in range(m)]
        maxC = [0 for _ in range(n)]
        for _, i, j in list1:
            res[i][j] = max(maxR[i], maxC[j]) + 1
            maxR[i] = res[i][j]
            maxC[j] = res[i][j]
        return res


'''
        m, n = len(grid), len(grid[0])
        def transform1(r, c):
            return r * n + c
        def transform2(node):
            return (node // n, node % n)

        dic = defaultdict(list)
        entry = [0 for _ in range(m * n)]
        for i in range(m):
            for j in range(n-1):
                first = transform1(i, j)
                second = transform1(i, j+1)
                if grid[i][j] < grid[i][j+1]:
                    dic[first].append(second)
                    entry[second] += 1
                else:
                    dic[second].append(first)
                    entry[first] += 1
        for i in range(n):
            for j in range(m-1):
                first = transform1(j, i)
                second = transform1(j+1, i)
                if grid[j][i] < grid[j+1][i]:
                    dic[first].append(second)
                    entry[second] += 1
                else:
                    dic[second].append(first)
                    entry[first] += 1
        res = [[0 for _ in range(n)] for _ in range(m)]
        deq = deque([i for i in range(m*n) if entry[i] == 0])
        index = 1
        while deq:
            leng = len(deq)
            for _ in range(leng):
                x = deq.popleft()
                x1, y1 = transform2(x)
                res[x1][y1] = index
                for node in dic[x]:
                    entry[node] -= 1
                    if entry[node] == 0:
                        deq.append(node)
            index += 1
        return res
'''