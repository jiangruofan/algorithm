class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        res = []
        sums.sort()
        judge = False

        def cal1(list1, cnt, val):
            list2 = []
            seen = Counter(list1)
            dic = Counter()
            for i in range(len(list1) - 1, -1, -1):
                num = list1[i]
                if num in dic:
                    list2.append(num)
                    dic[num] -= 1
                    if dic[num] == 0:
                        del dic[num]
                elif num - val in seen:
                    cnt -= 1
                    if cnt == 0:
                        list2 += list1[:i][::]
                        break
                    dic[num - val] += 1
                else:
                    break
                seen[num] -= 1
                if seen[num] == 0:
                    del seen[num]
            return list2

        def cal(n, list1, path):
            nonlocal judge, res
            if n == 1:
                if 0 not in list1:
                    return False
                res = path[::]
                res.append(list1[0] if list1[0] != 0 else list1[1])
                judge = True
                return

            val = list1[-1] - list1[-2]
            cnt = 2 ** n - 2 ** (n - 1)

            list2 = cal1(list1, cnt, val)
            if len(list2) == 2 ** (n - 1):
                path.append(val)
                cal(n - 1, list2[::-1], path)
                path.pop()

            if judge:
                return

            list2 = cal1(list1[::-1], cnt, -val)
            if len(list2) == 2 ** (n - 1):
                path.append(-val)
                cal(n - 1, list2, path)
                path.pop()

        cal(n, sums, [])
        return res
