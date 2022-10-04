class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if stack and nums[stack[-1][0]] < nums[i]:
                _, val = stack.pop()
                cnt = 0
                while stack and nums[stack[-1][0]] < nums[i]:
                    _, num = stack.pop()
                    if val < num:
                        val = num
                    else:
                        val += 1
                stack.append((i, val))
                res = max(res, val)
            else:
                stack.append((i, 1))
        return res


