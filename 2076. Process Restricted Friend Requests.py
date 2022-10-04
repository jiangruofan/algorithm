class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        opp = [set() for _ in range(n)]
        for i, j in restrictions:
            opp[i].add(j)
            opp[j].add(i)
        p = list(range(n))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        res = []
        for i, j in requests:
            a, b = find(i), find(j)
            if a in opp[b] or b in opp[a]:
                res.append(False)
            else:
                res.append(True)
                if a != b:
                    p[b] = a
                    for k in opp[b]:
                        opp[a].add(find(k))
        return res
