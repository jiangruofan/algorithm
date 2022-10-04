class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i, leng = 0, len(formula)

        def getNum():
            num = ''
            nonlocal i
            while i < leng and formula[i].isdigit():
                num += formula[i]
                i += 1
            return int(num) if len(num) > 0 else 1

        def getString():
            nonlocal i
            s = formula[i]
            i += 1
            while i < leng and formula[i].islower():
                s += formula[i]
                i += 1
            return s

        while i < leng:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                x = getNum()
                for key in stack[-1]:
                    stack[-1][key] *= x
                dic1 = stack.pop()
                for key, val in dic1.items():
                    stack[-1][key] += val
            else:
                s1 = getString()
                count = getNum() if i < leng and formula[i].isdigit() else 1
                stack[-1][s1] += count

        res = ''
        for key in sorted(stack[0].keys()):
            res += key + (str(stack[0][key]) if stack[0][key] != 1 else '')
        return res