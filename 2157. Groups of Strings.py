class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        dic = defaultdict(int)
        count = defaultdict(lambda: 1)
        total, max1 = len(words), 1

        def find(x: int):
            if dic[x] == x:
                return x
            dic[x] = find(dic[x])
            return dic[x]

        def merge(x: int, y: int):
            nonlocal total, max1
            if x not in dic or y not in dic:
                return
            fa1, fa2 = find(x), find(y)
            if fa1 == fa2:
                return
            dic[fa1] = fa2
            count[fa2] += count[fa1]
            total -= 1
            max1 = max(max1, count[fa2])

        for s in words:
            n = 0
            for s1 in s:
                n |= 1 << (ord(s1) - ord('a'))
            if n not in dic:
                dic[n] = n
            else:
                count[n] += 1
                total -= 1
                max1 = max(max1, count[n])

        for key in dic:
            for n in range(26):
                merge(key, key | (1 << n))
                if key & (1 << n):
                    for n1 in range(26):
                        if key & (1 << n1) == 0:
                            merge(key, key ^ (1 << n) | (1 << n1))
        return [total, max1]