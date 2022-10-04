class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        res = left = sum(tasks[i][0] for i in range(n))
        tasks.sort(key = lambda x : -(x[1] - x[0]))
        for x, y in tasks:
            if left < y:
                res += y - left
                left = y
            left -= x
        return res