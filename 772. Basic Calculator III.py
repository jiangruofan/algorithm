class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        s += " "
        def cal():
            nonlocal i
            stack = []
            sign = "+"
            num = "0"
            while i < len(s):
                if s[i] == "(":
                    i += 1
                    num = str(cal())
                if s[i].isdigit():
                    num += s[i]
                if (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:
                    if sign == "+":
                        stack.append(int(num))
                    elif sign == "-":
                        stack.append(-int(num))
                    elif sign == "*":
                        stack[-1] *= int(num)
                    elif sign == "/":
                        stack[-1] = int(stack[-1] / int(num))
                    sign = s[i]
                    num = ""
                if s[i] == ")":
                    i += 1
                    break
                i += 1
            return sum(stack)
        return cal()