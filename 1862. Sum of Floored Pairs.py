class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        min1, max1 = min(nums), max(nums)
        presum = Counter()

        for val in range(min1, max1+1):
            presum[val] = cnt[val] + presum[val-1]
        mod = 10 ** 9 + 7
        res = 0
        for begin in cnt:
            index = 1
            total = 0
            # 5 6 7 8 9 max1
            for val in range(begin, max1, begin):
                if val + begin > max1:
                    break
                total += index * (presum[val+begin-1] - presum[val-1])
                index += 1
            total += index * (presum[max1] - presum[max1 - max1 % begin - 1])
            total *= cnt[begin]
            total %= mod
            res += total
            res %= mod
        return res
