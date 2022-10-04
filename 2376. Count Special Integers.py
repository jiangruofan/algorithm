class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        num = str(n)
        leng = len(num)
        res = sum(9 * perm(9, i-1) for i in range(1, leng))
        seen = set()
        for i in range(leng):
            cnt = 0
            for j in range(int(num[i])):
                if i == 0 and j == 0:
                    continue
                if j not in seen:
                    cnt += 1
            res += cnt * perm(10-i-1, leng-i-1)
            if i == leng - 1 and int(num[i]) not in seen:
                res += 1
            if int(num[i]) in seen:
                break
            seen.add(int(num[i]))
        return res