class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = 0
        for i in range(k):
            list2 = []
            for j in range(i, n, k):
                list2.append(arr[j])
            cnt = []
            for j in range(len(list2)):
                x = bisect_right(cnt, list2[j])
                if x == len(cnt):
                    cnt.append(list2[j])
                else:
                    cnt[x] = list2[j]
            res += len(list2) - len(cnt)
        return res

