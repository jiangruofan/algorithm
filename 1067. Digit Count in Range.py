class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def cal(num):
            val = 1
            cnt = 0
            for i in range(len(str(num))):
                cur = num // val
                mid = cur % 10
                high = cur // 10
                if d == 0:
                    high -= 1

                cnt += high * val
                if mid > d:
                    cnt += val
                elif mid == d:
                    cnt += num - cur * val + 1
                val *= 10
            return cnt

        return cal(high) - cal(low - 1)