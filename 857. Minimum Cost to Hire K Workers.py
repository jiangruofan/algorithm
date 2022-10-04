class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # earned[i] / quality[i] = unit for i in range(k)
        # earned[i] >= wage[i] -> unit >= wage[i] / quality[i] for i in range(k)
        units = []
        n = len(quality)
        for i in range(n):
            units.append((wage[i]/quality[i], i))
        units.sort()
        heap = [-quality[units[i][1]] for i in range(k-1)]
        heapify(heap)
        total = -sum(heap)
        res = float('inf')
        for i in range(k-1, n):
            res = min(res, units[i][0] * (total + quality[units[i][1]]))
            heappush(heap, -quality[units[i][1]])
            total += quality[units[i][1]]
            total += heappop(heap)
        return res
