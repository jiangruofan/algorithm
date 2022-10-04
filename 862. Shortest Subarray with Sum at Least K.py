class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for val in nums:
            prefix.append(val + prefix[-1])
        deq = deque()
        res = float('inf')
        for i, val in enumerate(prefix):
            while deq and val - prefix[deq[0]] >= k:
                res = min(res, i - deq[0])
                deq.popleft()
            while deq and val <= prefix[deq[-1]]:
                deq.pop()
            deq.append(i)
        return res if res != float('inf') else -1
