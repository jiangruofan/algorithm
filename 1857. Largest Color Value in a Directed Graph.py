class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        if not edges:
            return 1

        dic = defaultdict(list)
        entry = Counter()
        nodes = set()
        record = defaultdict(lambda: Counter())

        for x, y in edges:
            entry[y] += 1
            dic[x].append(y)
            nodes.add(x)
            nodes.add(y)

        deq = deque([val for val in nodes if entry[val] == 0])
        res = -1
        while deq:
            x = deq.popleft()
            record[x][colors[x]] += 1
            if not dic[x]:
                for key in record[x]:
                    res = max(res, record[x][key])

            for node in dic[x]:
                for key in record[x]:
                    record[node][key] = max(record[node][key], record[x][key])
                entry[node] -= 1
                if entry[node] == 0:
                    deq.append(node)

        return res
