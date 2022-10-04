class Solution:
    def alienOrder(self, words: List[str]) -> str:
        entry = Counter()
        map1 = defaultdict(list)
        total = set(words[0])
        for i in range(1, len(words)):
            total.update(set(words[i]))
            min1 = min(len(words[i]), len(words[i-1]))
            for j in range(min1):
                if words[i-1][j] != words[i][j]:
                    entry[words[i][j]] += 1
                    if entry[words[i-1][j]] == 0:
                        entry[words[i-1][j]] = 0
                    map1[words[i-1][j]].append(words[i][j])
                    break
                if j == len(words[i]) - 1 and j == min1 - 1 and j < len(words[i-1]) - 1:
                    return ''
        res = ''
        deq = deque([key for key, val in entry.items() if val == 0])
        while deq:
            x = deq.popleft()
            res += x
            for val in map1[x]:
                entry[val] -= 1
                if entry[val] == 0:
                    deq.append(val)
        for val in entry.values():
            if val != 0:
                return ''
        res += ''.join(list(total - set(res)))
        return res