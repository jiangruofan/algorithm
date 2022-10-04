class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = 2
        first, second = intervals[0][1] - 1, intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= first:
                continue
            elif first < intervals[i][0] <= second:
                res += 1
                first = second
                second = intervals[i][1]
            else:
                res += 2
                first = intervals[i][1] - 1
                second = intervals[i][1]
        return res
