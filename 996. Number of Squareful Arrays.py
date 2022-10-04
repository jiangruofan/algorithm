class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        seen = [False for _ in range(n)]
        res = 0

        def judge(x):
            y = sqrt(x)
            return y - int(y) == 0

        def dfs(last, total):
            nonlocal res
            if total == n:
                res += 1
                return

            for i in range(n):
                if seen[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not seen[i - 1]:
                    continue
                if last == -1 or judge(nums[i] + last):
                    seen[i] = True
                    dfs(nums[i], total + 1)
                    seen[i] = False

        dfs(-1, 0)

        return res