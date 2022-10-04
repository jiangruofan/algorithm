class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        k = len(days[0])
        dic = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if flights[i][j] == 0:
                    continue
                dic[i].append(j)

        @cache
        def dfs(loc, day):
            if day == k:
                return 0
            res = dfs(loc, day + 1) + days[loc][day]
            for val in dic[loc]:
                res = max(res, days[val][day] + dfs(val, day + 1))
            return res

        return dfs(0, 0)