class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def calNum(prefix):
            total = 0
            num = 1
            last = prefix + 1
            while last * num - 1 < n:
                total += num
                num *= 10
            if n >= prefix * num:
                total += n - prefix * num + 1
            return total

        begin = 1
        while 1:
            num = calNum(begin)
            if num >= k:
                k -= 1
                if k == 0:
                    return begin
                begin *= 10
            else:
                k -= num
                begin += 1