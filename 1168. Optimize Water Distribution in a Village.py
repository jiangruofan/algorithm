class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        dic = defaultdict(lambda: defaultdict(lambda: float('inf')))
        res = 0
        for a, b, d in pipes:
            dic[a][b] = min(dic[a][b], d)
            dic[b][a] = min(dic[b][a], d)
        for i, val in enumerate(wells):
            dic[0][i+1] = val
            dic[i+1][0] = val
        heap = []
        seen = set([0])
        for key in dic[0]:
            heappush(heap, (dic[0][key], key))
        while len(seen) < n+1:
            while heap and heap[0][1] in seen:
                heappop(heap)
            dis, point = heappop(heap)
            seen.add(point)
            res += dis
            for key in dic[point]:
                if key not in seen:
                    heappush(heap, (dic[point][key], key))
        return res