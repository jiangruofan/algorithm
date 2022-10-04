class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        n = len(groups)
        cnt = [0 for _ in range(batchSize)]
        for val in groups:
            cnt[val % batchSize] += 1

        @cache
        def dfs(record, index, presum):
            if index == n:
                return 0
            record = list(record)

            res = 0
            for i, val in enumerate(record):
                if val == 0:
                    continue
                record[i] -= 1
                record1 = tuple(record)
                record[i] += 1
                res = max(res, dfs(record1, index + 1, (presum + i) % batchSize))
            add1 = 1 if presum % batchSize == 0 else 0
            return res + add1

        return dfs(tuple(cnt), 0, 0)