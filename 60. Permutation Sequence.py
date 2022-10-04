class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return "1"
        list1 = [i for i in range(1, n+1)]
        total = 1
        res = ""
        for i in range(2, n):
            total *= i
        sign = n - 1
        while k != 0:
            index = k // total if k % total == 0 else k // total + 1
            res += str(list1[index-1])
            list1.pop(index-1)
            k %= total
            total //= sign
            sign -= 1
        res += ''.join(list(map(str, list1[::-1])))
        return res

