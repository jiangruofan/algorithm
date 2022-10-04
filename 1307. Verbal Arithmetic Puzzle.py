class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        n = len(words)
        result = result[::-1]
        for i in range(n):
            if len(words[i]) > len(result):
                return False
            words[i] = words[i][::-1]

        dic = {}
        numbers = [False for i in range(10)]

        def dfs(r, c, total):
            if r == n:
                if result[c] in dic:
                    if total % 10 != dic[result[c]]:
                        return False
                    else:
                        return dfs(0, c + 1, total // 10)
                else:
                    if numbers[total % 10]:
                        return False
                    else:
                        numbers[total % 10] = True
                        dic[result[c]] = total % 10
                        if dfs(0, c + 1, total // 10):
                            return True
                        numbers[total % 10] = False
                        del dic[result[c]]
                        return False

            if c == len(result):
                return dic[result[-1]] != 0 and total == 0 if len(result) > 1 else total == 0

            if c >= len(words[r]):
                return dfs(r + 1, c, total)

            if words[r][c] in dic:
                if dic[words[r][c]] == 0 and c == len(words[r]) - 1 and len(words[r]) > 1:
                    return False
                return dfs(r + 1, c, total + dic[words[r][c]])
            else:
                for i in range(10):
                    if numbers[i]:
                        continue
                    if i == 0 and c == len(words[r]) - 1 and len(words[r]) > 1:
                        continue
                    numbers[i] = True
                    dic[words[r][c]] = i
                    if dfs(r + 1, c, total + i):
                        return True
                    numbers[i] = False
                    del dic[words[r][c]]
                return False

        return dfs(0, 0, 0)