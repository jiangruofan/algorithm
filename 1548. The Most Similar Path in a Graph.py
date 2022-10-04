class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        dic = defaultdict(list)
        for x, y in roads:
            dic[x].append(y)
            dic[y].append(x)
        dic[-1] = [i for i in range(n)]

        @cache
        def dfs(road, path):
            if path == len(targetPath):
                return [0, []]

            cur = 0 if road == -1 or names[road] == targetPath[path] else 1

            res = float('inf')
            res2 = []
            for node in dic[road]:
                num, list1 = dfs(node, path + 1)
                if num < res:
                    res = num
                    res2 = list1
            return [res + cur, [road] + res2]

        return dfs(-1, -1)[1][1:]