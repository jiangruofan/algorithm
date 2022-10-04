class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        fa = [i for i in range(m * n)]
        dic = defaultdict(list)
        entry = [0 for _ in range(m * n)]

        def find(node):
            if fa[node] == node:
                return node
            fa[node] = find(fa[node])
            return fa[node]

        def union(x, y):
            fa1 = find(x)
            fa2 = find(y)
            if fa1 != fa2:
                fa[fa1] = fa2

        for i in range(m):
            x = [(matrix[i][j], i * n + j) for j in range(n)]
            x.sort()
            for j in range(len(x) - 1):
                if x[j][0] == x[j + 1][0]:
                    union(x[j][1], x[j + 1][1])
                else:
                    dic[x[j][1]].append(x[j + 1][1])
                    entry[x[j + 1][1]] += 1

        for i in range(n):
            x = [(matrix[j][i], j * n + i) for j in range(m)]
            x.sort()
            for j in range(len(x) - 1):
                if x[j][0] == x[j + 1][0]:
                    union(x[j][1], x[j + 1][1])
                else:
                    dic[x[j][1]].append(x[j + 1][1])
                    entry[x[j + 1][1]] += 1

        group = defaultdict(list)
        for i in range(m):
            for j in range(n):
                father = find(i * n + j)
                print((i * n + j, father))
                group[father].append(i * n + j)
                if father != i * n + j:
                    entry[father] += entry[i * n + j]

        deq = deque([i for i, val in enumerate(entry) if val == 0 and fa[i] == i])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        rank = 1

        while deq:
            leng = len(deq)
            for _ in range(leng):
                x = deq.popleft()
                for val in group[x]:
                    res[val // n][val % n] = rank

                for val in group[x]:
                    for val1 in dic[val]:
                        entry[fa[val1]] -= 1
                        if entry[fa[val1]] == 0:
                            deq.append(fa[val1])
            rank += 1

        return res
