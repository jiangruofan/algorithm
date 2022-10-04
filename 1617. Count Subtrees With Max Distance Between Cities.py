class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)

        res = [0 for _ in range(n - 1)]

        def check(subtree):
            total = set(subtree)
            total.remove(subtree[0])
            deq = deque([subtree[0]])
            while deq:
                x = deq.popleft()
                for val in dic[x]:
                    if val not in total:
                        continue
                    total.remove(val)
                    deq.append(val)
            return False if total else True

        # 2 times BFS
        def cal(subtree):
            total = set(subtree)
            total.remove(subtree[0])
            deq = deque([subtree[0]])
            while deq:
                leng = len(deq)
                for i in range(leng):
                    x = deq.popleft()
                    for val in dic[x]:
                        if val not in total:
                            continue
                        total.remove(val)
                        deq.append(val)
                    if i == leng - 1 and not deq:
                        node1 = x

            dis = 0
            total = set(subtree)
            total.remove(node1)
            deq = deque([node1])
            while deq:
                leng = len(deq)
                for i in range(leng):
                    x = deq.popleft()
                    for val in dic[x]:
                        if val not in total:
                            continue
                        total.remove(val)
                        deq.append(val)
                dis += 1
            return dis - 1

        for bitmast in range(1, 1 << n):
            index = 1
            subtree = []
            while bitmast:
                if bitmast & 1:
                    subtree.append(index)
                index += 1
                bitmast >>= 1
            if len(subtree) < 2 or not check(subtree):
                continue

            res[cal(subtree) - 1] += 1

        return res