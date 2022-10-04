class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        mod = 10 ** 9 + 7
        @cache
        def dfs(num):
            if num == 0 or num == 2:
                return 1
            cnt = 0
            for i in range(2, num+1, 2):
                cnt += dfs(i-2) * dfs(num-i)
                cnt %= mod
            return cnt
        return dfs(numPeople) % mod