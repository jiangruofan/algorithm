class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []

        def cal(a, b):
            x = gcd(a, b)
            if x == 1:
                return 1
            return a * b // x

        k = 0
        while k < len(nums) + 1:
            while len(ans) > 1:
                count = cal(ans[-1], ans[-2])
                if count != 1:
                    ans.pop()
                    ans.pop()
                    ans.append(count)
                else:
                    break
            if k < len(nums):
                ans.append(nums[k])
            k += 1
        return ans