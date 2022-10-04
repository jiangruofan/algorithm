class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        l = 0
        sum1 = 0
        heap = []
        for i in range(n):
            sum1 += runningCosts[i]
            heappush(heap, (-chargeTimes[i], i))
            while heap[0][1] < l:
                heappop(heap)
            if -heap[0][0] + (i - l + 1) * sum1 > budget:
                sum1 -= runningCosts[l]
                l += 1
        return n - l

#         leng = len(chargeTimes)
#         l, r = 0, leng

#         def check(n):
#             heap = [(-chargeTimes[i], i) for i in range(n-1)]
#             heapify(heap)
#             sum1 = sum(runningCosts[:n-1])
#             for i in range(n-1, leng):
#                 heappush(heap, (-chargeTimes[i], i))
#                 sum1 += runningCosts[i]
#                 while heap[0][1] <= i - n:
#                     heappop(heap)
#                 if -heap[0][0] + n * sum1 <= budget:
#                     return True
#                 sum1 -= runningCosts[i-n+1]
#             return False


#         while l < r:
#             mid = (l + r + 1) // 2
#             if check(mid):
#                 l = mid
#             else:
#                 r = mid - 1
#         return l