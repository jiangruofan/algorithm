class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        def findFather(m, c, t):
            res = []
            if t == 1:
                for val in graph[c]:
                    if val == 0:
                        continue
                    res.append((m, val, 2))
            else:
                for val in graph[m]:
                    res.append((val, c, 1))
            return res

        def findChild(m, c, t):
            if t == 1:
                for val in graph[m]:
                    if list1[val][c][2] != 2:
                        return True
            else:
                for val in graph[c]:
                    if val == 0:
                        continue
                    if list1[m][val][1] != 1:
                        return True
            return False

        leng = len(graph)
        deq = deque()
        list1 = [[[0 for _ in range(3)] for _ in range(leng)] for _ in range(leng)]
        for i in range(1, leng):
            deq.append((0, i, 2))
            list1[0][i][2] = 1
            deq.append((i, i, 1))
            deq.append((i, i, 2))
            list1[i][i][1] = 2
            list1[i][i][2] = 2
        while deq:
            mouth, cat, t = deq.popleft()
            father = findFather(mouth, cat, t)
            for mouth_fa, cat_fa, t_fa in father:
                if list1[mouth_fa][cat_fa][t_fa] != 0:
                    continue
                if t + list1[mouth][cat][t] == 3 or not findChild(mouth_fa, cat_fa, t_fa):
                    list1[mouth_fa][cat_fa][t_fa] = list1[mouth][cat][t]
                    deq.append((mouth_fa, cat_fa, t_fa))
        return list1[1][2][1]