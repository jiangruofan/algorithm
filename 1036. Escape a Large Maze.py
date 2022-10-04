class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(list(map(tuple, blocked)))
        n = len(blocked) * (len(blocked) - 1) // 2
        def bfs(begin, target):
            deq = deque([(begin[0], begin[1])])
            seen = {(begin[0], begin[1])}
            while deq:
                x = deq.popleft()
                for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    i, j = x[0] + a, x[1] + b
                    if 0 <= i < 1000000 and 0 <= j < 1000000 and (i, j) not in blocked and (i, j) not in seen:
                        if i == target[0] and j == target[1]:
                            return True
                        if len(seen) + 1 > n:
                            return True
                        deq.append((i, j))
                        seen.add((i, j))
            return False
        return bfs(source, target) and bfs(target, source)