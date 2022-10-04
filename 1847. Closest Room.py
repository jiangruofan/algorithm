class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:

        def lowbit(x):
            return x & (-x)

        dic = defaultdict(list)

        def add(size, id1):
            i = size
            while i > 0:
                dic[i].append(id1)
                i -= lowbit(i)

        def query(minsize, id1):
            ans = -1
            diff = float('inf')
            i = minsize
            while i <= maxsize:
                if not dic[i]:
                    i += lowbit(i)
                    continue
                index = bisect_left(dic[i], id1)
                if index < len(dic[i]):
                    if abs(id1 - dic[i][index]) < diff:
                        diff = abs(id1 - dic[i][index])
                        ans = dic[i][index]
                    elif abs(id1 - dic[i][index]) == diff:
                        ans = min(ans, dic[i][index])
                if index - 1 >= 0:
                    if abs(id1 - dic[i][index - 1]) < diff:
                        diff = abs(id1 - dic[i][index - 1])
                        ans = dic[i][index - 1]
                    elif abs(id1 - dic[i][index - 1]) == diff:
                        ans = min(ans, dic[i][index - 1])
                i += lowbit(i)
            return ans

        maxsize = 0
        for _, size in rooms:
            maxsize = max(maxsize, size)

        for id1, size in rooms:
            add(size, id1)

        for key in dic:
            dic[key].sort()

        res = []
        for id1, size in queries:
            res.append(query(size, id1))

        return res