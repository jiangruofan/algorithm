class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        dic = defaultdict(list)
        for i, val in enumerate(s):
            if len(dic[val]) < 2:
                dic[val].append(i)
                dic[val].append(i)
            else:
                dic[val][1] = i

        x = []
        for val in dic:
            l = dic[val][0]
            judge = True
            i = l
            while i < dic[val][1]:
                if dic[s[i]][0] < l:
                    judge = False
                    break
                dic[val][1] = max(dic[val][1], dic[s[i]][1])
                i += 1
            if judge:
                x.append((l, dic[val][1]))

        res = []
        x = sorted(list(x), key=lambda x: (x[1], x[1] - x[0]))
        for i, (l, r) in enumerate(x):
            if not res:
                res.append(s[l:r + 1])
                last = r
                continue
            if l > last:
                res.append(s[l:r + 1])
                last = r
        return res