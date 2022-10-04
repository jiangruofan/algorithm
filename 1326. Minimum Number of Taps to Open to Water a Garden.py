class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        list1 = [0 for _ in range(n + 1)]
        for i, val in enumerate(ranges):
            l = max(0, i - val)
            list1[l] = max(list1[l], min(i + val, n))

        res = 0
        i = 0
        end = 0
        maxleng = 0
        while i <= end:
            maxleng = max(maxleng, list1[i])
            if maxleng >= n:
                return res + 1
            if i == end:
                end = maxleng
                res += 1
            i += 1
        return -1

