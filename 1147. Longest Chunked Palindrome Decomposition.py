class Solution:
    def longestDecomposition(self, text: str) -> int:
        leng = len(text)
        dp = [0 for _ in range(leng+1)]
        p = 131
        mod = 10 ** 9 + 7
        p1 = [0 for _ in range(leng+1)]
        p1[0] = 1
        for i in range(1, leng+1):
            p1[i] = p1[i-1] * p % mod
        for i, s in enumerate(text):
            total = dp[i] * p + ord(s)
            total %= mod
            dp[i+1] = total
        l, r = 1, leng
        prel, prer = 0, leng + 1
        cnt = 0
        while l < r:
            left = dp[l] - dp[prel] * p1[l - prel] % mod
            left %= mod
            right = dp[prer-1] - dp[r-1] * p1[prer - r] % mod
            right %= mod
            if left == right:
                cnt += 2
                prel = l
                prer = r
                if r - l == 1:
                    cnt -= 1
            l += 1
            r -= 1
        return cnt + 1