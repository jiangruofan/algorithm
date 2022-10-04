class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        n = len(nums)
        total = Counter()
        cnt = Counter()
        res = 0
        for i, val in enumerate(nums):
            if total[cnt[val]] > 0:
                total[cnt[val]] -= 1
            if total[cnt[val]] == 0:
                del total[cnt[val]]
            cnt[val] += 1
            total[cnt[val]] += 1
            if len(total) == 1 and (1 in total or 1 in total.values()):
                res = max(res, i+1)
            if len(total) == 2:
                if total[1] == 1 or (total[max(total.keys())] == 1 and max(total.keys()) - min(total.keys()) == 1):
                    res = max(res, i+1)
        return res
