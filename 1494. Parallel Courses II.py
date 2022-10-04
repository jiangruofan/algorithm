class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k1: int) -> int:
        leng = 1 << n
        pre = [0 for _ in range(leng)]
        dp = [20 for _ in range(leng)]
        dp[0] = 0
        for x, y in relations:
            pre[y] |= 1 << (x - 1)

        for i in range(leng):
            candidates = []
            for j in range(n):
                if not i & (1 << j) and pre[j+1] & i == pre[j+1]:
                    candidates.append(j)
            for val in combinations(candidates, min(k1, len(candidates))):
                x = 0
                for val1 in val:
                    x |= 1 << val1
                dp[i+x] = min(dp[i+x], dp[i]+1)
        return dp[-1]