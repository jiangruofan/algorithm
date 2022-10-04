class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        res = 0
        n = len(matrix[0])
        list1 = [0 for _ in range(n)]
        matrix.insert(0, [0 for _ in range(n)])
        m = len(matrix)
        for i in range(1, m):
            for k in range(n):
                list1[k] += matrix[i][k]
            list2 = [0 for _ in range(n)]
            for j in range(i):
                for k in range(n):
                    list2[k] += matrix[j][k]
                list3 = [list1[k] - list2[k] for k in range(n)]
                list3 = [0] + list3
                dic = Counter()
                dic[0] += 1
                for i in range(1, len(list3)):
                    list3[i] = list3[i] + list3[i-1]
                    res += dic[list3[i] - target]
                    dic[list3[i]] += 1
        return res