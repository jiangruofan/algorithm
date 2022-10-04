class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)

        cnt = [0 for _ in range(n)]
        in1 = [0 for _ in range(n)]
        out = [0 for _ in range(n)]
        clock = 0

        def cal(node, fa):
            nonlocal cnt, in1, out, clock
            clock += 1
            in1[node] = clock

            res = nums[node]
            for val in dic[node]:
                if val == fa:
                    continue
                res ^= cal(val, node)

            cnt[node] = res
            out[node] = clock
            return res

        cal(0, -1)

        for i in range(len(edges)):
            if in1[edges[i][0]] < in1[edges[i][1]]:
                edges[i][0], edges[i][1] = edges[i][1], edges[i][0]

        res = float('inf')
        for (x, y), (x1, y1) in combinations(edges, 2):
            if in1[y] >= in1[x1] and out[x1] >= in1[y]:
                a, b, c = cnt[0] ^ cnt[x1], cnt[x], cnt[x1] ^ cnt[x]
            elif in1[y1] >= in1[x] and out[x] >= in1[y1]:
                a, b, c = cnt[0] ^ cnt[x], cnt[x1], cnt[x] ^ cnt[x1]
            else:
                a, b, c = cnt[x], cnt[x1], cnt[0] ^ cnt[x] ^ cnt[x1]
            res = min(res, max(a, b, c) - min(a, b, c))
        return res