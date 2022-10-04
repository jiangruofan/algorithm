class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)
        word = ""
        for key in sorted(cnt.keys(), reverse=True):
            num = cnt[key] // k
            word += key * num

        def check(x):
            index = 0
            for s1 in s:
                if s1 == x[index]:
                    index += 1
                    if index == len(x):
                        return True
            return False

        for i in range(len(word), 0, -1):
            for list1 in permutations(word, i):
                x = list1 * k
                if check(x):
                    return ''.join(list1)

        return ""