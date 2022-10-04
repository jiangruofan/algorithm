class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        seen = set()
        res = 0
        mod = 10 ** 7
        p = [1]
        leng = len(text)
        for _ in range(leng):
            p.append(p[-1] * 131 % mod)

        rolling = [0]
        for i in range(leng):
            rolling.append(rolling[-1] * 131 % mod + ord(text[i]))

        for i in range(leng):
            for j in range(i + 1):
                # j ... i i+1 i+1+i-j
                r = 2 * i - j + 1
                if r >= leng:
                    continue
                x = rolling[i + 1] - rolling[j] * p[i - j + 1] % mod
                x %= mod
                if x in seen:
                    continue
                y = rolling[r + 1] - rolling[i + 1] * p[i - j + 1] % mod
                y %= mod
                if x == y:
                    res += 1
                    seen.add(x)
        return res
