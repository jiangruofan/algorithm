class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        def parse(s):
            s1 = list(s)
            if len(s) == 1:
                return [int(s)]
            elif len(s) == 2:
                return [int(s), int(s1[0]) + int(s1[1])]
            else:
                return [int(s), int(s1[0]) + int(s1[1]) + int(s1[2]), int(s[:2]) + int(s1[2]), int(s1[0]) + int(s[1:])]

        def begin(s):
            s = list(s)
            ans = []
            i = 0
            while i < len(s):
                if s[i].isalpha():
                    ans.append(s[i])
                    i += 1
                    continue
                get = ""
                while i < len(s) and s[i].isdigit():
                    get += s[i]
                    i += 1
                ans.append(get)
            return ans

        @cache
        def dfs(i, num1, j, num2):
            if i == len(s1) and j == len(s2):
                return num1 == num2
            if i == len(s1) and num1 == 0:
                return False
            if j == len(s2) and num2 == 0:
                return False

            if i < len(s1) and s1[i][0].isdigit():
                x = parse(s1[i])
                for val in x:
                    if dfs(i + 1, num1 + val, j, num2):
                        return True
                return False
            elif j < len(s2) and s2[j][0].isdigit():
                x = parse(s2[j])
                for val in x:
                    if dfs(i, num1, j + 1, num2 + val):
                        return True
                return False

            if num1 != 0 and num2 != 0:
                min1 = min(num1, num2)
                return dfs(i, num1 - min1, j, num2 - min1)
            elif num1 == 0 and num2 != 0:
                return dfs(i + 1, num1, j, num2 - 1)
            elif num1 != 0 and num2 == 0:
                return dfs(i, num1 - 1, j + 1, num2)
            else:
                if s1[i] != s2[j]:
                    return False
                return dfs(i + 1, num1, j + 1, num2)

        s1 = begin(s1)
        s2 = begin(s2)
        return dfs(0, 0, 0, 0)