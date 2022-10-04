class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        dic = defaultdict(set)
        for x, y in mappings:
            dic[y].add(x)
        n = len(s)
        m = len(sub)
        for i in range(n-m+1):
            judge = True
            for j in range(i, i+m):
                if sub[j-i] not in dic[s[j]] and sub[j-i] != s[j]:
                    judge = False
                    break
            if judge:
                return True
        return False
