class Solution:
    def minOperationsToFlip(self, expression: str) -> int:

        # x1 the first number to become 0, y1 the first number to become 1
        # x2 the second number to become 0, y2 the second number to become 1
        def cal1(x1, y1, x2, y2, judge):
            if judge == "&":
                return (min(x1 + y2, x2 + y1, x1 + x2, 1 + x1 + x2), min(y1 + y2, 1 + min(y1 + x2, y2 + x1, y1 + y2)))
            elif judge == "|":
                return (min(x1 + x2, 1 + min(x1 + y2, x2 + y1, x1 + x2)), min(y1 + x2, y2 + x1, y1 + y2, 1 + y1 + y2))
            else:
                return (x2, y2)

        index = 0

        def cal():
            nonlocal index
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0
            sign = "#"
            while index < len(expression):
                if expression[index].isdigit():
                    x2 = 0 if int(expression[index]) == 0 else 1
                    y2 = 0 if int(expression[index]) == 1 else 1
                    index += 1

                if index < len(expression) and expression[index] == "(":
                    index += 1
                    x2, y2 = cal()

                if index == len(expression) or expression[index] == ")" or expression[index] == "&" or expression[
                    index] == "|":
                    x1, y1 = cal1(x1, y1, x2, y2, sign)
                    if index < len(expression):
                        sign = expression[index]
                    if index < len(expression) and expression[index] == ")":
                        index += 1
                        break
                    index += 1

            return (x1, y1)

        return max(cal())