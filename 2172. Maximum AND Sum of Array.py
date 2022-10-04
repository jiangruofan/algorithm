class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @cache
        def dfs(index, a, b):
            if index >= len(nums):
                return 0
            max1 = 0
            for i in range(1, numSlots + 1):
                if a >> i & 1 == 0:
                    max1 = max(max1, (nums[index] & i) + dfs(index+1, a | (1 << i), b))
                elif b >> i & 1 == 0:
                    max1 = max(max1, (nums[index] & i) + dfs(index+1, a, b | (1 << i)))
            return max1
        return dfs(0, 0, 0)