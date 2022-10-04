class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sum1 = sum(target)
        for i in range(len(target)):
            target[i] = -target[i]
        heap = target
        heapify(heap)
        while heap:
            if heap[0] == -1:
                return True
            x = -heappop(heap)
            if sum1 <= x:
                return False
            sum1 -= x
            val = x - sum1 * max(1, (x + heap[0]) // sum1) if heap else x - sum1
            sum1 += val
            if val < 1:
                return False
            heappush(heap, -val)
