class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        n = len(stations)
        i = 0
        while i < n and stations[i][0] <= startFuel:
            heappush(heap, -stations[i][1])
            i += 1
        x = startFuel
        res = 0
        while heap and x < target:
            x += -heappop(heap)
            while i < n and stations[i][0] <= x:
                heappush(heap, -stations[i][1])
                i += 1
            res += 1
        return res if x >= target else -1
