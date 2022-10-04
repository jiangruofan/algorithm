class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        dic = defaultdict(list)
        for i, val in enumerate(parent):
            if i == 0:
                continue
            dic[val].append(i)
        res = 1

        def dfs(node):
            nonlocal res
            if not dic[node]:
                return 1
            list1 = []
            for val in dic[node]:
                if s[val] == s[node]:
                    dfs(val)
                    continue
                heappush(list1, -dfs(val))
            first = 0
            if list1:
                first = -heappop(list1)
            second = 0
            if list1:
                second = -heappop(list1)
            res = max(res, 1 + first + second)
            return first + 1

        dfs(0)
        return res