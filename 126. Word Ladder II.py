class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        dic = defaultdict(list)
        if beginWord not in wordList:
            wordList.append(beginWord)
        for val in wordList:
            for i in range(len(val)):
                new = val[:i] + "#" + val[i+1:]
                dic[val].append(new)
                dic[new].append(val)
        set1 = set([beginWord])
        set2 = set([endWord])
        deq1 = deque([(beginWord, 1, [beginWord])])
        deq2 = deque([(endWord, 1, [endWord])])
        while deq1 and deq2:
            dic1 = defaultdict(list)
            leng = len(deq1)
            same = set()
            for _ in range(leng):
                word, index, path = deq1.popleft()
                for val in dic[word]:
                    if val in set1:
                        continue
                    same.add(val)
                    if index % 2 == 0:
                        newpath = [s for s in path] + [val]
                        deq1.append((val, index+1, newpath))
                        dic1[val].append(newpath)
                    else:
                        newpath = [s for s in path]
                        deq1.append((val, index+1, newpath))
                        dic1[val].append(newpath)
            set1.update(same)

            leng = len(deq2)
            same = set()
            res = []
            for _ in range(leng):
                word, index, path = deq2.popleft()
                for val in dic[word]:
                    if val in dic1:
                        for list1 in dic1[val]:
                            res.append(list1 + path[::-1])
                    if val in set2:
                        continue
                    same.add(val)
                    if index % 2 == 0:
                        deq2.append((val, index+1, [s for s in path] + [val]))
                    else:
                        deq2.append((val, index+1, [s for s in path]))
            set2.update(same)
            if res:
                return res
        return []