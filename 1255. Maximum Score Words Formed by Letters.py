class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters = Counter(letters)
        res = 0
        list1 = [Counter(word) for word in words]
        origin = (1 << len(words)) - 1
        x = origin
        while x:
            cnt = Counter()
            x1 = x
            index = 0
            while x1:
                if x1 & 1:
                    cnt.update(list1[index])
                x1 >>= 1
                index += 1
            judge = True
            total = 0
            for key in cnt:
                total += cnt[key] * score[ord(key)-ord('a')]
                if cnt[key] > letters[key]:
                    judge = False
                    break
            if judge:
                res = max(res, total)
            x = (x - 1) & origin
        return res
