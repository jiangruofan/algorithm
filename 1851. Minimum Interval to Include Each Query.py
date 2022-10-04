class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i, val in enumerate(queries):
            dic[val].append(i)

        queries.sort()
        intervals.sort()
        heap = []
        index = 0
        res = [-1 for _ in range(len(queries))]
        for i, val in enumerate(queries):
            if i > 0 and queries[i] == queries[i - 1]:
                continue
            while index < len(intervals) and intervals[index][0] <= val:
                heappush(heap, (intervals[index][1] - intervals[index][0] + 1, intervals[index][1]))
                index += 1
            while heap and heap[0][1] < val:
                heappop(heap)
            if heap:
                for index1 in dic[val]:
                    res[index1] = heap[0][0]

        return res