class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        nums = Counter()
        for word in words:
            x = set(word)
            val = 0
            for s in x:
                val |= 1 << (ord(s) - ord('a'))
            nums[val] += 1

        res = []
        for word in puzzles:
            x = set(word)
            x.remove(word[0])
            val = 0
            for s in x:
                val |= 1 << (ord(s) - ord('a'))
            cnt = nums[1 << (ord(word[0]) - ord('a'))]
            index = val
            while index:
                cnt += nums[index + (1 << (ord(word[0]) - ord('a')))]
                index = (index - 1) & val
            res.append(cnt)
        return res

