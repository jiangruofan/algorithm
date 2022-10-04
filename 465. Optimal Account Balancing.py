class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        dic = defaultdict(int)
        for x, y, val in transactions:
            dic[x] -= val
            dic[y] += val
            if dic[x] == 0:
                del dic[x]
            if dic[y] == 0:
                del dic[y]

        n = len(dic)
        list1 = list(dic.values())
        total = [0 for _ in range(1 << n)]
        for i in range(1 << n):
            index = 0
            num = i
            while num:
                if num & 1:
                    total[i] += list1[index]
                num >>= 1
                index += 1

        def cal(num):
            total = 0
            while num:
                if num & 1:
                    total += 1
                num >>= 1
            return total

        dp = [0 for _ in range(1 << n)]
        for i in range(1, 1 << n):
            if total[i] != 0:
                continue
            dp[i] = cal(i) - 1
            j = i
            while j:
                if total[j] == 0:
                    dp[i] = min(dp[i], dp[j] + dp[i - j])
                j = (j - 1) & i

        return dp[-1]
