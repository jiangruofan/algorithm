class Solution:
    def evaluate(self, expression: str) -> int:
        expression = deque(list(expression))

        def get1(stack, flag, dic):
            if stack[0] == "let":
                for i in range(1, len(stack) - 1, 2):
                    if stack[i + 1]:
                        dic[stack[i]] = dic.get(stack[i + 1], stack[i + 1])
                return dic if flag else dic.get(stack[-1], stack[-1])

            x, y = int(dic.get(stack[1], stack[1])), int(dic.get(stack[2], stack[2]))
            return str(x + y if stack[0] == "add" else x * y)

        def cal(expression, dic):
            stack = [""]
            res = None
            while expression:
                x = expression.popleft()
                if x == "(":
                    if stack[0] == "let":
                        new_dic = get1(stack, 1, dict(dic))
                        stack[-1] += cal(expression, new_dic)
                    else:
                        stack[-1] += cal(expression, dic)
                elif x == " ":
                    stack.append("")
                elif x == ")":
                    res = get1(stack, 0, dict(dic))
                    break
                else:
                    stack[-1] += x
            return res if res else stack[0]

        return int(cal(expression, {}))

