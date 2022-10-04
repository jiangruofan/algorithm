class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        leng = len(s)

        # bound : 0 no restriction
        # boung : 1 higher bound
        @cache
        def dfs(pos, state, bound):
            if pos == leng:
                return 1
            res = 0
            r = int(s[pos]) if bound else 9
            for i in range(r + 1):
                if i == 0 and state == 0:
                    res += dfs(pos + 1, state, 0)
                    continue
                if state & (1 << i):
                    continue
                new_state = state | (1 << i)
                new_bound = 0
                if bound == 1 and i == r:
                    new_bound = 1
                res += dfs(pos + 1, new_state, new_bound)
            return res

        return n + 1 - dfs(0, 0, 1)
