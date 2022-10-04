class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        nums = [val[1] for val in envelopes]
        list1 = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > list1[-1]:
                list1.append(nums[i])
            else:
                list1[bisect_left(list1, nums[i])] = nums[i]
        return len(list1)