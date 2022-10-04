class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_num = len(words)
        total = word_len * word_num
        res = []
        for i in range(word_len):
            dic = Counter(words)
            l = i
            for r in range(i+word_len, len(s)+1, word_len):
                s1 = s[r-word_len:r]
                dic[s1] -= 1
                if dic[s1] == 0:
                    del dic[s1]
                if r - l == total:
                    if len(dic) == 0:
                        res.append(l)
                    s1 = s[l:l+word_len]
                    dic[s1] += 1
                    if dic[s1] == 0:
                        del dic[s1]
                    l += word_len
        return res
