class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [0 for _ in range(n)]
        cnt = [0 for _ in range(n)]
        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)

        def cal(node, fa, level):
            nonlocal res, cnt
            res[0] += level
            for val in dic[node]:
                if val == fa:
                    continue
                cnt[node] += cal(val, node, level + 1)
            cnt[node] += 1
            return cnt[node]

        def dfs(node, fa, num):
            nonlocal res
            res[node] = num + n - 2 * cnt[node]
            for val in dic[node]:
                if val == fa:
                    continue
                dfs(val, node, res[node])

        cal(0, -1, 0)
        for val in dic[0]:
            dfs(val, 0, res[0])
        return res


'''
total[0] = self[0] + self[2] + node_num[2]
total[2] = self[2] + self[0] + node_num[0]
total[0] = total[2] + node_num[2] - node_num[0]
total[2] = total[0] + node_num[0] - node_num[2]
'''