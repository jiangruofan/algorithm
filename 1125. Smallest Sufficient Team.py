class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dic = {req_skills[i]:i for i in range(len(req_skills))}
        path = defaultdict(list)
        dp = [float('inf') for _ in range(1 << len(req_skills))]
        dp[0] = 0
        for i in range(1, len(people)+1):
            set1 = set([dic[val] for val in people[i-1]])
            for j in range(1 << len(req_skills)):
                x = j
                for val in set1:
                    x |= 1 << val
                if dp[j] + 1 < dp[x]:
                    dp[x] = dp[j] + 1
                    path[x] = path[j][::] + [i-1]
        return path[(1 << len(req_skills))-1]
    
    
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dic = {s : i for i, s in enumerate(req_skills)}
        leng = len(req_skills)
        dp = [float('inf') for _ in range(1<<leng)]
        dp[0] = 0
        path = {}
        for i in range(len(people)):
            x = 0
            for s in people[i]:
                x |= 1 << dic[s]
            for j in range(1<<leng):
                y = j - (j & x)
                if dp[y] + 1 < dp[j]:
                    dp[j] = dp[y] + 1
                    path[j] = (y, i)
        res = []
        cur = (1<<leng) - 1
        while cur != 0:
            res.append(path[cur][1])
            cur = path[cur][0]
        return res





        
