class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ans = ""
        mod = 10 ** (n - 1)
        seen = set()
        def dfs(node):
            nonlocal ans
            for i in range(k):
                x = node * 10 + i
                if x not in seen:
                    seen.add(x)
                    dfs(x % mod)
                    ans += str(i)
        dfs(0)
        return ans + (n - 1) * "0"