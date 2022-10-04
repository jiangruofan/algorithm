class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = -float('inf')
        deq = deque([(points[0][1] - points[0][0], points[0][0])])
        for i in range(1, len(points)):
            x = points[i][0]
            y = points[i][1]
            while deq and x - deq[0][1] > k:
                deq.popleft()
            res = max(res, x + y + deq[0][0] if deq else -float('inf'))
            while deq and deq[-1][0] <= y - x:
                deq.pop()
            deq.append((y - x, x))
        return res