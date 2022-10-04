class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dic = defaultdict(list)
        if beginWord not in wordList:
            wordList.append(beginWord)
        for s in wordList:
            for i in range(len(s)):
                x = s[:i] + "*" + s[i+1:]
                dic[s].append(x)
                dic[x].append(s)
        deq1 = deque([beginWord])
        deq2 = deque([endWord])
        seen1 = set()
        seen2 = set()
        index1 = index2 = 1
        while deq1 and deq2:
            leng = len(deq1)
            for _ in range(leng):
                x = deq1.popleft()
                for val in dic[x]:
                    if val not in seen1:
                        deq1.append(val)
                        seen1.add(val)
            index1 += 1

            leng = len(deq2)
            for _ in range(leng):
                x = deq2.popleft()
                for val in dic[x]:
                    if val in deq1:
                        return (index1 + index2 + 1) // 2
                    if val not in seen2:
                        deq2.append(val)
                        seen2.add(val)
            index2 += 1
        return 0