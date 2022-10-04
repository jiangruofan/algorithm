class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        cnt = Counter(nums)
        n = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cnt_prime = Counter()
        for val in n:
            x = 0
            for i, val1 in enumerate(prime):
                if val % val1 == 0:
                    x |= 1 << i
            cnt_prime[val] = x

        dp = [0 for _ in range(1 << 10)]
        dp[0] = 1
        for val in n:
            if not cnt[val]:
                continue
            for i in range(len(dp)):
                if cnt_prime[val] & i == 0:
                    dp[cnt_prime[val] | i] += dp[i] * cnt[val]

        return (sum(dp) - 1) * (2 ** cnt[1]) % mod