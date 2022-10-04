class Solution:
    def kEmptySlots(self, bulbs1: List[int], k: int) -> int:
        if k >= len(bulbs1):
            return -1
        bulbs = [0 for _ in range(len(bulbs1))]
        for i, val in enumerate(bulbs1):
            bulbs[val-1] = i + 1
        res = float('inf')
        seen = set()
        heap = [bulbs[i] for i in range(1, 1+k)] if k != 0 else [float('inf')]
        heapify(heap)
        for i in range(k+1, len(bulbs)):
            while seen and heap[0] in seen:
                seen.remove(heap[0])
                heappop(heap)
            if heap[0] > bulbs[i] and heap[0] > bulbs[i-k-1]:
                res = min(res, max(bulbs[i], bulbs[i-k-1]))
            heappush(heap, bulbs[i])
            seen.add(bulbs[i-k])
        return res if res != float('inf') else -1