class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        saved = defaultdict(list)
        for x, y, dis in edgeList:
            saved[dis].append((x, y))
        list1 = deque(sorted(saved.keys()))
        dic = defaultdict(list)
        for i, (_, _, dis) in enumerate(queries):
            dic[dis].append(i)

        fa = [i for i in range(n)]

        def find(node):
            if node == fa[node]:
                return node
            fa[node] = find(fa[node])
            return fa[node]

        def union(x, y):
            fa1 = find(x)
            fa2 = find(y)
            if fa1 != fa2:
                fa[fa1] = fa2

        res = [False for _ in range(len(queries))]
        for dis in sorted(dic.keys()):
            while list1 and list1[0] < dis:
                for x, y in saved[list1[0]]:
                    union(x, y)
                list1.popleft()

            for index in dic[dis]:
                res[index] = True if find(queries[index][0]) == find(queries[index][1]) else False

        return res

