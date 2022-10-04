class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        n = len(words[0])
        res = []

        for word in words:
            for i in range(len(word)):
                dic[word[:i + 1]].append(word)

        def dfs(path):
            if len(path) == n:
                res.append(path[::])
                return
            x = len(path)
            prefix = ""
            for i in range(x):
                prefix += path[i][x:x + 1]
            for val in dic[prefix]:
                path.append(val)
                dfs(path)
                path.pop()

        for word in words:
            dfs([word])
        return res