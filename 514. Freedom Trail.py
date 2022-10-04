class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dic = defaultdict(list)
        for i, s in enumerate(ring):
            dic[s].append(i)
        dp = [defaultdict(lambda: float('inf')) for _ in range(len(key))]
        leng = len(ring)
        for val in dic[key[0]]:
            dp[0][val] = min(val, leng-val)
        for i in range(1, len(key)):
            for cur in dic[key[i]]:
                for pre in dic[key[i-1]]:
                    dp[i][cur] = min(dp[i][cur], dp[i-1][pre] + min(abs(cur-pre), leng-abs(cur-pre)))
        return min(dp[-1].values()) + len(key)

