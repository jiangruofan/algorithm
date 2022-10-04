from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        cnt = [0 for _ in range(k)]
        heap = []
        list1 = SortedList(range(k))
        n = len(arrival)
        for i in range(n):
            while heap and heap[0][0] <= arrival[i]:
                list1.add(heappop(heap)[1])
            index = list1.bisect_left(i % k)
            if not list1:
                continue
            if index == len(list1):
                x = list1.pop(0)
            else:
                x = list1.pop(index)
            cnt[x] += 1
            heappush(heap, (arrival[i] + load[i], x))
        max1 = max(cnt)
        return [i for i, val in enumerate(cnt) if val == max1]
