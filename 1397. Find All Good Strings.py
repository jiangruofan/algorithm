class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        mod = 10 ** 9 + 7
        leng = len(evil)
        next1 = [0 for _ in range(leng)]
        for i in range(1, leng):
            x = next1[i - 1]
            while x > 0 and evil[i] != evil[x]:
                x = next1[x - 1]
            if evil[i] == evil[x]:
                next1[i] = x + 1
        '''
        bound: 0 no restriction
        bound: 1 lower bound
        bound: 2 higher bound
        bound: 3 both bound
        '''

        # xxxxxxx abcdef g xxxxx
        #         abcdef h
        @cache
        def cal(state, s):
            while state > 0 and evil[state] != s:
                state = next1[state - 1]
            return state + 1 if evil[state] == s else 0

        @cache
        def dfs(pos, state, bound):
            if state == leng:
                return 0
            if pos == n:
                return 1
            res = 0
            l = ord(s1[pos]) if bound & 1 else ord('a')
            r = ord(s2[pos]) if bound & 2 else ord('z')
            for i in range(l, r + 1):
                new_state = cal(state, chr(i))
                new_bound = 0
                if bound == 3 and i == l and i == r:
                    new_bound = 3
                elif bound & 1 and i == l:
                    new_bound = 1
                elif bound & 2 and i == r:
                    new_bound = 2
                res += dfs(pos + 1, new_state, new_bound)
                res %= mod
            return res

        return dfs(0, 0, 3)

