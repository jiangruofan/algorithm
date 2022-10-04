class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def check(x):
            list1 = []
            while x:
                list1.append(x % k)
                x //= k
            l, r = 0, len(list1) - 1
            while l < r:
                if list1[l] != list1[r]:
                    return False
                l += 1
                r -= 1
            return True

        def cal(x, flag):
            if flag:
                return  int(str(x) + str(x)[:-1][::-1])
            else:
                return int(str(x) + str(x)[::-1])

        res = 0
        total = 0
        leng = 1
        while 1:
            begin = 10 ** (leng - 1)
            end = 10 ** leng
            for i in range(begin, end):
                x = cal(i, True)
                if check(x):
                    total += 1
                    res += x
                    if total == n:
                        return res
            for i in range(begin, end):
                x = cal(i, False)
                if check(x):
                    total += 1
                    res += x
                    if total == n:
                        return res
            leng += 1

