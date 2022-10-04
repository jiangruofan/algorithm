class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        leng = len(favorite)
        entry = [0] * leng
        for val in favorite:
            entry[val] += 1
        list1 = [0] * leng
        deq = deque([i for i, val in enumerate(entry) if val == 0])
        while deq:
            x = deq.popleft()
            list1[x] += 1
            list1[favorite[x]] = max(list1[favorite[x]], list1[x])
            entry[favorite[x]] -= 1
            if entry[favorite[x]] == 0:
                deq.append(favorite[x])
        res1 = 0
        res2 = 0
        for i, val in enumerate(entry):
            if val == 0:
                continue
            ans = 0
            x = i
            while entry[favorite[x]] != 0:
                entry[favorite[x]] -= 1
                ans += 1
                x = favorite[x]
            if ans > 2:
                res1 = max(res1, ans)
            else:
                res2 += ans + list1[i] + list1[favorite[i]]
        return max(res1, res2)