class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        total = 0
        leng = len(nums)
        for i in range(leng):
            if nums[i] >= 0:
                total += nums[i]
            else:
                nums[i] = -nums[i]
        nums.sort()
        res = total
        heap = [(-total + nums[0], 0)]
        for _ in range(k-1):
            val, index = heappop(heap)
            res = -val
            if index < leng - 1:
                heappush(heap, (val+nums[index+1], index+1))
                heappush(heap, (val-nums[index]+nums[index+1], index+1))
        return res