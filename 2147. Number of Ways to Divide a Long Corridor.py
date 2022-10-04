class Solution:
    def numberOfWays(self, corridor: str) -> int:
        num1 = corridor.count('S')
        if num1 % 2 == 1 or num1 == 0:
            return 0
        elif num1 == 2:
            return 1
        sum1 = 0
        index = 0
        res = 1
        judge = False
        for i, s in enumerate(corridor):
            if s == 'S':
                sum1 += 1
                if sum1 % 2 == 0:
                    index = i
                    judge = True
                else:
                    if judge:
                        res *= i - index
        return res % (10 ** 9 + 7)