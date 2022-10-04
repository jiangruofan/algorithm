class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deq = deque()
        res = -float('inf')
        for i, val in enumerate(nums):
            while deq and i - deq[0][1] > k:
                deq.popleft()
            num = max(val, val + (deq[0][0] if deq else 0))
            while deq and deq[-1][0] < num:
                deq.pop()
            deq.append((num, i))
            res = max(res, num)
        return res
