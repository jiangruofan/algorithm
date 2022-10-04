class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = list(target)
        m, n = len(stamp), len(target)
        res = []
        cnt = 0

        def check(index):
            l = 0
            cnt = 0
            for i in range(index, index + m):
                if target[i] == "?":
                    l += 1
                    continue
                elif stamp[l] == target[i]:
                    cnt += 1
                    l += 1
                else:
                    return (False, -1)
            return (True, cnt)

        while cnt < n:
            cur = cnt
            for i in range(n - m + 1):
                judge, num = check(i)
                if judge:
                    cnt += num
                    target[i:i + m] = ["?"] * m
                    if num > 0:
                        res.append(i)
            if cur == cnt:
                return []
        return res[::-1]
