class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        presum = [0]
        for val in nums:
            presum.append(presum[-1] + val)

        cnt = Counter()
        for i in range(1, len(nums)):
            cnt[presum[-1] - presum[i] * 2] += 1

        res = max(cnt[0], cnt[-(nums[0] - k)])
        cntl = Counter()
        for i in range(1, len(nums)):
            total = 0
            cntl[presum[-1] - presum[i] * 2] += 1
            cnt[presum[-1] - presum[i] * 2] -= 1
            total += cnt[-(nums[i] - k)]
            total += cntl[-(k - nums[i])]
            res = max(res, total)

        return res