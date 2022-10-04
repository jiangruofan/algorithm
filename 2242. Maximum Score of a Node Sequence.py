class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        dic = defaultdict(list)
        for x, y in edges:
            heappush(dic[x], (scores[y], y))
            heappush(dic[y], (scores[x], x))
            if len(dic[x]) == 4:
                heappop(dic[x])
            if len(dic[y]) == 4:
                heappop(dic[y])
        res = -1
        for x, y in edges:
            for (i, j), (i1, j1) in product(dic[x], dic[y]):
                if j != y and j1 != x and j != j1:
                    res = max(res, scores[x] + scores[y] + i + i1)

        return res