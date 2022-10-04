class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        cnt = Counter(nums)
        nums = sorted(cnt.values(), reverse=True)[:len(quantity)]
        quantity.sort(reverse=True)

        def dfs(nums, index):
            if index == len(quantity):
                return True

            for i in range(len(nums)):
                if nums[i] >= quantity[index]:
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    nums[i] -= quantity[index]
                    if dfs(nums, index + 1):
                        return True
                    nums[i] += quantity[index]
            return False

        return dfs(nums, 0)