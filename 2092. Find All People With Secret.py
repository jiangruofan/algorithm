class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dic = defaultdict(set)
        dic_time = defaultdict(set)
        for x, y, time in meetings:
            dic[time].add((x, y))
            dic_time[time].add(x)
            dic_time[time].add(y)
        res = set([0, firstPerson])
        for key in sorted(dic.keys()):
            dic1 = defaultdict(set)
            for x, y in dic[key]:
                dic1[x].add(y)
                dic1[y].add(x)
            deq = deque([val for val in dic_time[key] if val in res])
            while deq:
                x = deq.popleft()
                for val in dic1[x]:
                    if val in res:
                        continue
                    deq.append(val)
                    res.add(val)

        return list(res)
