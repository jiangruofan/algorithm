class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diff = [0 for _ in range(n+1)]
        res = 0
        for i, val in enumerate(nums):
            if i > 0:
                diff[i] += diff[i-1]
            real = 1 - val if diff[i] % 2 == 1 else val
            if real == 1:
                continue
            res += 1
            diff[i] += 1
            if i + k > n:
                return -1
            diff[i+k] -= 1
        return res