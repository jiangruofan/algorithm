class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0 for _ in range(n+1)]
        for i, val in enumerate(nums):
            if val <= i:
                diff[0] += 1
                diff[i-nums[i]+1] -= 1
                diff[i+1] += 1
                diff[-1] -= 1
            else:
                diff[i+1] += 1
                diff[n-1-nums[i]+1+i+1] -= 1
        for i in range(1, n):
            diff[i] += diff[i-1]

        min1 = max(diff[:-1])
        for i in range(n):
            if diff[i] == min1:
                return i

'''
0 1 2 3 4 5
x x x x x x
        2
if nums[i] <= i:
    diff[0:i-nums[i]] = 1
    diff[i-nums[i]+1:i] = 0
    diff[i+1:] = 1

0 1 2 3 4 5
x x x x x x
    4
if nums[i] > i:
    diff[0:i] = 0
    diff[i+1:n-1-nums[i]+1+i] = 1
    diff[n-1-nums[i]+1+i+1:] = 0    
'''