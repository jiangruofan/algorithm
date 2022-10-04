class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0

        def cal(s1, sign):
            nonlocal ans
            left = right = res = 0
            for val in s1:
                if val == sign:
                    left += 1
                else:
                    if right + 1 > left:
                        right = left = 0
                    else:
                        right += 1
                        if left == right:
                            res = max(res, left * 2)
            ans = max(ans, res)

        cal(s, '(')
        cal(s[::-1], ')')
        return ans
