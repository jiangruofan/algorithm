class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        cnt = [Counter() for _ in range(len(words[0]))]
        for word in words:
            for i, s in enumerate(word):
                cnt[i][s] += 1
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(len(words[0]))] for _ in range(len(target))]
        for i in range(len(target)):
            for j in range(len(words[0])):
                dp[i][j] += dp[i][j-1] if j > 0 else 0
                if target[i] in cnt[j]:
                    dp[i][j] += (dp[i-1][j-1] if i > 0 and j > 0 else 0 if i > 0 else 1) * cnt[j][target[i]]
                dp[i][j] %= mod
        return dp[-1][-1]