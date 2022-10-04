class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(hats)
        dp = [0 for _ in range(1 << n)]
        dp[0] = 1
        dic = defaultdict(list)
        for i, list1 in enumerate(hats):
            for val in list1:
                dic[val].append(i)

        for hat in range(1, 41):
            if not dic[hat]:
                continue
            for i in range((1 << n) - 1, -1, -1):
                for val in dic[hat]:
                    if (1 << val) & i:
                        continue
                    dp[i + (1 << val)] += dp[i]
                    dp[i + (1 << val)] %= mod

        return dp[-1]