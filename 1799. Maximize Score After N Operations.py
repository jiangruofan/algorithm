class Solution:
    def maxScore(self, nums: List[int]) -> int:
        leng = len(nums)
        dp = [0 for _ in range(1<<leng)]
        def cal(num):
            index = 0
            res = []
            while num:
                if num & 1:
                    res.append(nums[index])
                num >>= 1
                index += 1
            return gcd(res[0], res[1])

        for i in range(1<<leng):
            if i.bit_count() % 2:
                continue
            num = i.bit_count()
            if num == 2:
                dp[i] = cal(i)
                continue
            index = i
            while index:
                if index.bit_count() == num - 2:
                    x = cal(i^index)
                    dp[i] = max(dp[i], dp[i&index] + x * (num // 2))
                index = (index - 1) & i
        return dp[-1]