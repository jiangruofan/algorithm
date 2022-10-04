class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        for i in range(1, len(stoneValue)):
            stoneValue[i] += stoneValue[i-1]
        stoneValue = [0] + stoneValue
        @cache
        def dfs(i):
            if i >= len(stoneValue):
                return 0
            max1 = -float(inf)
            for j in range(1, 4):
                max1 = max(max1, stoneValue[-1] - stoneValue[i-1] - dfs(i+j))
            return max1
        x = dfs(1)
        if x > stoneValue[-1] - x:
            return "Alice"
        elif x < stoneValue[-1] - x:
            return "Bob"
        else:
            return "Tie"