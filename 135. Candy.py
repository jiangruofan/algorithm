class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        list1 = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                list1[i] = list1[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                list1[i] = max(list1[i+1] + 1, list1[i])
        return sum(list1)