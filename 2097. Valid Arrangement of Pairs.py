class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        entry = Counter()
        out = Counter()
        for x, y in pairs:
            dic[x].append(y)
            entry[y] += 1
            out[x] += 1

        for key in out:
            begin = key
            if out[key] > entry[key]:
                break

        path = []

        def dfs(node):
            while dic[node]:
                dfs(dic[node].pop())
            path.append(node)

        dfs(begin)
        res = []
        for i in range(len(path) - 1, 0, -1):
            res.append([path[i], path[i - 1]])
        return res