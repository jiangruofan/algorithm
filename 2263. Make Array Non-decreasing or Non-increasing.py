class Solution:
    def convertArray(self, nums: List[int]) -> int:

        def cal(nums):
            heap = []
            res = 0
            for val in nums:
                if heap and -heap[0] > val:
                    res += -heap[0] - val
                    heappop(heap)
                    heappush(heap, -val)
                heappush(heap, -val)
            return res

        return min(cal(nums), cal(nums[::-1]))