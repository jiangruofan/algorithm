class Solution:
    def shortestPalindrome(self, s: str) -> str:
        res = -1
        base = 131
        mod = 10 ** 9 + 7
        left = right = 0
        index = 1
        for i, val in enumerate(s):
            left = (left * base + ord(val)) % mod
            right += ord(val) * index
            right %= mod
            if left == right:
                res = i
            index *= base
            index %= mod
        return s[res+1:][::-1]+s if res != -1 else s[::-1] + s

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        saved = s
        s = s + s[::-1]
        leng = len(s)
        l = r = 0
        cnt = 0
        list1 = [0 for _ in range(leng)]
        for i in range(leng):
            if i > r:
                l = r = i
                while r < leng and s[r] == s[r-i]:
                    r += 1
                list1[i] = r - l
                if i >= leng // 2 and r == leng:
                    cnt = r - l
                    break
                r -= 1
            else:
                if list1[i-l] + i - 1 < r:
                    list1[i] = list1[i-l]
                else:
                    l = i
                    while r < leng and s[r] == s[r-i]:
                        r += 1
                    list1[i] = r - l
                    if i >= leng // 2 and r == leng:
                        cnt = r - l
                        break
                    r -= 1

        return saved[cnt:][::-1] + saved
