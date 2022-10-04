class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        list1 = sorted(range(n), key=lambda x : efficiency[x])
        res = 0
        mod = 10 ** 9 + 7
        total = 0
        heap = []
        for i in range(n-1, -1, -1):
            total += speed[list1[i]]
            heappush(heap, speed[list1[i]])
            if len(heap) > k:
                total -= heappop(heap)
            res = max(res, total * efficiency[list1[i]])
        return res % mod