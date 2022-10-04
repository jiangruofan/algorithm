class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        leng = len(words)
        left = set([i for i in range(leng)])

        @cache
        def cal(pre, after):
            for i in range(len(after), 0, -1):
                if pre.endswith(after[:i]):
                    return after[i:]
            return after

        @cache
        def dfs(left, last):
            if len(left) == 0:
                return last
            res = ""
            for index in left:
                ans = dfs(left - {index}, words[index]) + cal(words[index], last)
                if not res or len(ans) < len(res):
                    res = ans
            return res

        res = ""
        for i, word in enumerate(words):
            x = dfs(frozenset(left) - {i}, word)
            if not res or len(x) < len(res):
                res = x
        return res

