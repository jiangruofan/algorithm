class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        mod = 2 ** 64
        res = []
        dic = {}
        for i, s in enumerate(words):
            dic[s] = i

        def cal(i, word, judge):
            forward = backword = 0
            p = 1
            for j in range(len(word)):
                s = word[j:j + 1]
                forward += ord(s) * p
                backword *= 131
                backword += ord(s)
                forward %= mod
                backword %= mod
                p *= 131
                if backword == forward:
                    s1 = word[j + 1:][::-1] if judge else word[j + 1:]
                    if s1 in dic:
                        res.append([dic[s1], i] if judge else [i, dic[s1]])
            s1 = word[::-1]
            if s1 in dic and dic[s1] != i:
                res.append([dic[s1], i] if judge else [i, dic[s1]])

        for i, word in enumerate(words):
            cal(i, word, True)
            cal(i, word[::-1], False)

        return res