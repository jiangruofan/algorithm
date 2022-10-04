class Solution:
    def nearestPalindromic(self, n: str) -> str:
        res = []
        if int(n) <= 10:
            return str(int(n) - 1)
        if int(n) == 11:
            return "9"
        if int(n[::-1]) == 1:
            return str(int(n) - 1)
        if set(n) == {"9"}:
            return str(int(n) + 2)
        index = (len(n) + 1) // 2
        first = n[:index]
        second = n[index:]
        for val in (str(int(first) - 1), str(int(first)), str(int(first) + 1)):
            res.append(val+val[:len(second)][::-1])
        res.sort()
        ans = res[0]
        for val in res:
            if abs(int(val)) - abs(int(n)) < abs(int(n)) - abs(int(ans)) and val != n:
                ans = val
        return ans