class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = [0 for _ in range(n)]
        available = [i for i in range(n)]
        heapify(available)
        heap = []
        for start, end in meetings:
            while heap and heap[0][0] <= start:
                _, index = heappop(heap)
                heappush(available, index)
            if not available:
                end_time, index = heappop(heap)
                res[index] += 1
                heappush(heap, (end_time + end - start, index))
            else:
                index = heappop(available)
                res[index] += 1
                heappush(heap, (end, index))
        max1 = 0
        res_index = 0
        for i in range(n):
            if res[i] > max1:
                max1 = res[i]
                res_index = i
        return res_index