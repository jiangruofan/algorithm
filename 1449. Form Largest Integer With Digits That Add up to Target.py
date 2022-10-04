class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cost1 = Counter()
        for i, val in enumerate(cost):
            if val > target:
                continue
            cost1[val] = max(cost1[val], i + 1)
        list1 = list(cost1.keys())

        def check(str1, str2):
            if len(str1) > len(str2):
                return True
            elif len(str1) == len(str2) and trans(str1) > trans(str2):
                return True
            return False

        def trans(str):
            return "".join(sorted(list(str), reverse=True))

        dp = ["#" for _ in range(target + 1)]
        dp[0] = ""
        for val in list1:
            for i in range(1, target + 1):
                if i - val < 0 or dp[i - val] == "#":
                    continue
                if check(dp[i - val] + str(cost1[val]), dp[i]):
                    dp[i] = trans(dp[i - val] + str(cost1[val]))

        return dp[-1] if dp[-1] != "#" else "0"