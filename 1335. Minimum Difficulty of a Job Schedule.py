class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        leng = len(jobDifficulty)
        @cache
        def dfs(index:int, day:int):
            if day == d:
                return max(jobDifficulty[index:])
            max1 = 0
            ans = float('inf')
            for i in range(index, leng-d+day):
                max1 = max(max1, jobDifficulty[i])
                ans = min(ans, max1 + dfs(i+1, day+1))
            return ans if ans != float('inf') else -1
        return dfs(0, 1)