class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        res = []
        cnt = 0
        last = 0
        for i, val in enumerate(s):
            cnt += 1 if val == "1" else -1
            if cnt == 0:
                res.append("1" + self.makeLargestSpecial(s[last+1:i]) + "0")
                last = i + 1
        res.sort(reverse=True)
        return "".join(res)