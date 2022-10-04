class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = [("", set())]
        def cal(sign, exp):
            if sign == "!":
                return 1 - list(exp)[0]
            elif sign == "&":
                return 0 if 0 in exp else 1
            else:
                return 1 if 1 in exp else 0

        for s in expression:
            if s in ["!", "&", "|"]:
                stack.append((s, set()))
            elif s == "f" or s == "t":
                stack[-1][1].add(1 if s == "t" else 0)
            elif s == ")":
                sign, exp = stack.pop()
                stack[-1][1].add(cal(sign, exp))
        res = stack[0][1].pop()
        return True if res == 1 else False