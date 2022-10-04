class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        leng = len(nums)
        sign = [0 for _ in range(leng)]
        res = [-1 for _ in range(leng)]
        dicl = Counter()
        dicr = Counter()
        dic = defaultdict(lambda: Counter())
        max1 = 0
        for i in range(leng-1, -1, -1):
            res[i] = max1
            index = removeQueries[i]
            sign[index] = 1
            l = r = index
            total = nums[index]
            if index - 1 >= 0 and sign[index-1]:
                l = dicr[index-1]
                total += dic[l][index-1]
            if index + 1 < leng and sign[index+1]:
                r = dicl[index+1]
                total += dic[index+1][r]
            dicl[l] = r
            dicr[r] = l
            dic[l][r] = total
            max1 = max(max1, total)
        return res
