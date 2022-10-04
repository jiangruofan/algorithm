class Solution:
    def nextPalindrome(self, num: str) -> str:
        num1 = list(num[:len(num)//2])
        res = ''
        for i in range(len(num1)-2, -1, -1):
            if num1[i] >= num1[i+1]:
                continue
            for j in range(len(num1)-1, 0, -1):
                if num1[j] <= num1[i]:
                    continue
                num1[j], num1[i] = num1[i], num1[j]
                break
            res = ''.join(num1[:i+1]) + ''.join(sorted(num1[i+1:]))
            break
        if not res:
            return ''
        addtion = '' if len(num) % 2 == 0 else num[len(num) // 2]
        res = res + addtion + res[::-1]
        return res