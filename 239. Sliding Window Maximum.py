class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dic = Counter()
        heap = []
        res = []
        for i in range(len(nums)):
            heappush(heap, -nums[i])
            dic[nums[i]] += 1
            if i >= k - 1:
                while -heap[0] not in dic:
                    heappop(heap)
                res.append(-heap[0])
                dic[nums[i-k+1]] -= 1
                if dic[nums[i-k+1]] == 0:
                    del dic[nums[i-k+1]]
        return res