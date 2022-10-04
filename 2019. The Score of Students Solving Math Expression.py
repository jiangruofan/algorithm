class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        stack = []
        sign = "+"
        num = 0
        for i, val in enumerate(s):
            if val.isdigit():
                num = int(val)
            if val == "+" or val == "*" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                else:
                    stack[-1] *= num
                sign = val

        correct = sum(stack)

        @cache
        def cal(s):
            if len(s) == 1:
                return set([int(s)])

            res = set()
            for i, val in enumerate(s):
                if val == "+" or val == "*":
                    list1 = cal(s[:i])
                    list2 = cal(s[i + 1:])
                    for val1 in list1:
                        for val2 in list2:
                            x = val1 + val2 if val == "+" else val1 * val2
                            if x > 1000:
                                continue
                            res.add(x)

            return res

        total = cal(s)
        cnt = Counter(answers)
        res = 0
        for val in cnt:
            if val == correct:
                res += 5 * cnt[val]
            elif val in total:
                res += 2 * cnt[val]
        return res
