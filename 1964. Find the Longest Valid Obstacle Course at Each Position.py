class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        x = []
        res = []
        for val in obstacles:
            index = bisect_right(x, val)
            res.append(index+1)
            if index == len(x):
                x.append(val)
            else:
                x[index] = val
        return res