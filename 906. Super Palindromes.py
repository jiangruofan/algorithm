class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)
        res = 0
        for i in range(10 ** 9):
            x1 = str(i) + str(i)[0:-1][::-1]
            x2 = str(i) + str(i)[::-1]
            if int(x1) ** 2 > right:
                break
            x11 = str(int(x1) ** 2)
            x22 = str(int(x2) ** 2)
            if x11 == x11[::-1] and int(x11) >= left and int(x11) <= right:
                res += 1
            if x22 == x22[::-1] and int(x22) >= left and int(x22) <= right:
                res +=1
        return res