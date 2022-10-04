class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        dic = defaultdict(list)
        for i, val in enumerate(routes):
            for val1 in val:
                dic[val1].append(i)
        seen_stop = set()
        seen_bus = set()
        deq = deque([(source, 0)])
        seen_stop.add(source)
        while deq:
            stop, dis = deq.popleft()
            for val in dic[stop]:
                if val not in seen_bus:
                    seen_bus.add(val)
                    for val1 in routes[val]:
                        if val1 == target:
                            return dis + 1
                        if val1 not in seen_stop:
                            seen_stop.add(val1)
                        deq.append((val1, dis+1))
        return -1
