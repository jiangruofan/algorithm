class Solution:
    def isNumber(self, s: str) -> bool:
        def check(s1, num):
            if not s1:
                return False
            dot_num = 0
            for i in range(len(s1)):
                if s1[i] == ".":
                    dot_num += 1
                    if dot_num > num:
                        return False
                if i == 0:
                    continue
                if s1[i] == "+" or s1[i] == "-":
                    return False
            if s1[0] in ["+", "-"]:
                s1 = s1[1:]
            if not s1 or s1 == ".":
                return False
            return True

        for i, val in enumerate(s):
            if s[i].isdigit():
                continue
            if val not in ["e", "E", "+", "-", "."]:
                return False
        if "e" not in s and "E" not in s:
            return check(s, 1)
        if "e" in s:
            list1 = s.split("e")
        else:
            list1 = s.split("E")
        if len(list1) != 2:
            return False
        return check(list1[0], 1) and check(list1[1], 0)