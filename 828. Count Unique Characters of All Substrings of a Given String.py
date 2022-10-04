class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dic = defaultdict(list)
        for i, val in enumerate(s):
            dic[val].append(i)

        n = len(s)
        res = 0
        for list1 in dic.values():
            list1 = [-1] + list1 + [n]
            for i in range(1, len(list1) - 1):
                l = list1[i] - list1[i - 1]
                r = list1[i + 1] - list1[i]
                res += l * r
        return res