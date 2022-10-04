class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        center = right = -1
        p = [0 for _ in range(n)]
        for i in range(n):
            if i <= right:
                j = 2 * center - i
                r = min(p[j], right - i)
            else:
                r = 0
            while i - r >= 0 and i + r < n and s[i - r] == s[i + r]:
                r += 1
            p[i] = r - 1
            if i + p[i] > right:
                right = i + p[i]
                center = i

        l = [0 for _ in range(n)]
        l[0] = 1
        x = 0
        for i in range(1, n):
            while p[x] + x < i:
                x += 1
            l[i] = max(l[i - 1], (i - x) * 2 + 1)

        r = [0 for _ in range(n)]
        r[-1] = 1
        x = n - 1
        for i in range(n - 2, -1, -1):
            while x - p[x] > i:
                x -= 1
            r[i] = max(r[i + 1], (x - i) * 2 + 1)

        res = 0
        for i in range(n - 1):
            res = max(res, l[i] * r[i + 1])
        return res