class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        mod = 10 ** 9 + 7
        dic = defaultdict(list)
        for i in range(1, len(prevRoom)):
            dic[prevRoom[i]].append(i)

        factorial = [1]
        for i in range(1, len(prevRoom)):
            factorial.append(factorial[-1] * i % mod)

        @cache
        def fastPower(x, y):
            if y == 1:
                return x

            val = fastPower(x, y // 2)
            val *= val
            return val % mod if y % 2 == 0 else val * x % mod

        @cache
        def inv(x):
            return fastPower(x, mod - 2)

        def dfs(node):
            if not dic[node]:
                return (1, 1)

            multi = 1
            repeated = 1
            num = 0
            for val in dic[node]:
                x, y = dfs(val)
                num += x
                repeated *= inv(factorial[x])
                repeated %= mod
                multi *= y
                multi %= mod

            planNumber = factorial[num] * repeated * multi % mod
            return (num + 1, planNumber)

        return dfs(0)[1]