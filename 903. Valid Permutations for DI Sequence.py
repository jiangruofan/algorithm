'''
increase
2 1 0 [1] -> 3 2 0 [1]
decrease
1 0 2 [1] -> 2 0 3 [1]
0 2 1 [1] -> 0 3 2 [1]
'''
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s) + 1
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            new = [0 for _ in range(n)]
            total = sum(dp[h] for h in range(i))
            total %= mod
            for j in range(i+1):
                if s[i-1] == "I":
                    new[j] = new[j-1] + dp[j-1] if j > 0 else 0
                    new[j] %= mod
                else:
                    new[j] = total
                    total -= dp[j]
                    new[j] %= mod
            dp = new
        return sum(dp) % mod
