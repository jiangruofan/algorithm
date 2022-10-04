class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)
        deq = deque([(s1, 0)])
        seen = set([s1])
        res = 0
        while deq:
            leng = len(deq)
            for _ in range(leng):
                s, index = deq.popleft()
                for i in range(index, n):
                    if i == n - 1 and s[i] == s2[i]:
                        return res
                    if s[i] != s2[i]:
                        for j in range(i+1, n):
                            if s[j] == s2[i]:
                                new = s[:i] + s2[i] + s[i+1:j] + s[i] + s[j+1:]
                                if new not in seen:
                                    deq.append((new, i+1))
                                    seen.add(new)
                        break
            res += 1
