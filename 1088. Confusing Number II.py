class Solution:
    def confusingNumberII(self, n: int) -> int:
        numbers = [0, 1, 6, 8, 9]
        res = 0
        dic = {'1':'1', '6':'9', '9':'6', '8':'8', '0':'0'}
        def check(val):
            val = str(val)
            l, r = 0, len(val) - 1
            while l < r:
                if val[r] != dic[val[l]]:
                    return True
                l += 1
                r -= 1
            if l == r and val[l] in ["6", "9"]:
                return True
            return False

        def dfs(val):
            nonlocal res
            if val > n:
                return
            if check(val):
                res += 1
            for val1 in numbers:
                dfs(val * 10 + val1)
        for i in range(1, len(numbers)):
            dfs(numbers[i])
        return res

# valid number: 0 1 6 8 9