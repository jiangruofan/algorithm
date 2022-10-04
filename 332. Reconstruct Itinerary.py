class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        dic = defaultdict(list)
        for x, y in tickets:
            heappush(dic[x], y)
        res = []
        def dfs(node):
            while dic[node]:
                dfs(heappop(dic[node]))
            res.append(node)
        dfs("JFK")
        return res[::-1]