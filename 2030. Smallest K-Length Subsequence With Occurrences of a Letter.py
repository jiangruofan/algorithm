class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        cnt = Counter(s)
        delete = cnt[letter] - repetition
        deletetotal = len(s) - k
        stack = []
        for i, val in enumerate(s):
            while deletetotal > 0 and stack and stack[-1] > val and (stack[-1] != letter or delete > 0):
                x = stack.pop()
                deletetotal -= 1
                if x == letter:
                    delete -= 1
            stack.append(val)

        res = ""
        while deletetotal:
            if stack[-1] != letter:
                deletetotal -= 1
            else:
                if delete > 0:
                    delete -= 1
                    deletetotal -= 1
                else:
                    res += letter
            stack.pop()
        res = "".join(stack) + res[::-1]
        return res