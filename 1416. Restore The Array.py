class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10 ** 9 + 7
        leng = len(s)
        dp = [0 for _ in range(leng)]
        for i in range(leng):
            for j in range(i, -1, -1):
                if int(s[j:i+1]) > k or i - j > 10:
                    break
                if s[j] == "0":
                    continue
                dp[i] += dp[j-1] if j > 0 else 1
                dp[i] %= mod
        return dp[-1]