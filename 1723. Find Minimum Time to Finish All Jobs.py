class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        l = max(jobs)
        r = sum(jobs)
        jobs.sort(reverse=True)

        def check(index):
            if index == len(jobs):
                return True

            for i in range(k):
                if limit[i] < jobs[index]:
                    continue
                if i > 0 and limit[i] == limit[i - 1]:
                    continue
                limit[i] -= jobs[index]
                if check(index + 1):
                    return True
                limit[i] += jobs[index]

            return False

        while l < r:
            mid = (l + r) // 2
            limit = [mid for _ in range(k)]
            if check(0):
                r = mid
            else:
                l = mid + 1

        return l