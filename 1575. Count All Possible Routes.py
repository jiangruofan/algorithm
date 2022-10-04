class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        leng = len(locations)
        mod = 10 ** 9 + 7
        @cache
        def dfs(loc, left):
            if abs(locations[loc] - locations[finish]) > left:
                return 0
            res = 1 if loc == finish else 0
            for i in range(leng):
                if i == loc:
                    continue
                res += dfs(i, left-abs(locations[loc] - locations[i]))
            return res % mod
        return dfs(start, fuel)