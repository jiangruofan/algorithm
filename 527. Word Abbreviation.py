class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        dic = defaultdict(list)
        res = ["" for i in range(len(words))]
        for i, s in enumerate(words):
            words[i] = list(s)
            n = len(s)
            if n < 4:
                res[i] = s
                continue
            new = s[0] + str(n - 2) + s[-1]
            dic[(new, n - 2)].append(i)

        while dic:
            new_dic = defaultdict(list)
            for key in dic:
                if len(dic[key]) == 1:
                    if len(key[0]) < len(words[dic[key][0]]):
                        res[dic[key][0]] = key[0]
                    else:
                        res[dic[key][0]] = "".join(words[dic[key][0]])
                    continue
                for i in dic[key]:
                    cnt = key[1] - 1
                    word = words[i]
                    l = len(word)
                    new_dic[("".join(word[:l - cnt - 1]) + str(cnt) + word[-1], cnt)].append(i)
            dic = new_dic
        return res