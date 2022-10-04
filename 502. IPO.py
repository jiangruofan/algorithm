class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        n = len(profits)
        list1 = [(capital[i], profits[i]) for i in range(n)]
        list1.sort(key=lambda x: x[0])
        index = 0
        for _ in range(k):
            while index < n and list1[index][0] <= w:
                heappush(heap, -list1[index][1])
                index += 1
            if not heap:
                break
            w += -heappop(heap)
        return w



