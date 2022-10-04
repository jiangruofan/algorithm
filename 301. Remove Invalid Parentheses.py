class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s1):
            cnt = 0
            for val in s1:
                if val == "(":
                    cnt += 1
                elif val == ")":
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        set1 = set([s])
        while set1:
            res = []
            for val in set1:
                if isValid(val):
                    res.append(val)
            if res:
                return res
            set2 = set()
            for val in set1:
                for i in range(len(val)):
                    if i > 0 and val[i] == val[i - 1]:
                        continue
                    if val[i] in "(" or ")":
                        set2.add(val[:i] + val[i + 1:])
            set1 = set2
        return [""]