class Solution:
    def minJumps(self, arr: List[int]) -> int:
        leng = len(arr)
        dic = defaultdict(list)
        for i, val in enumerate(arr):
            dic[val].append(i)
        deq = deque([(0, 0)])
        seen = set([0])
        while deq:
            x, y = deq.popleft()
            if x == leng - 1:
                return y
            for i in [x + 1, x - 1] + dic[arr[x]]:
                if 0 <= i < leng and i not in seen:
                    deq.append((i, y + 1))
                    seen.add(i)
            dic[arr[x]] = []

        '''
        错误在于初始化path的时候 对于相同的值只加入右半边的相同值的对应下标
        错误举例
        [1,2,3,4,5,6,7,8,9,16,20,12,13,14,15,16,1,17,18,19,21,22,23,24,20]
        leng = len(arr)
        path = defaultdict(list)
        road = defaultdict(list)
        road[arr[-1]].append(leng-1)
        for i in range(leng-2, -1, -1):
            path[i].append(i+1)
            path[i].extend(road[arr[i]])
            if i - 1 > -1:
                path[i].append(i-1)
            road[arr[i]].append(i)
        deq = deque([(0, 0)])
        seen = set([0])
        while deq:
            x, y = deq.popleft()
            if x == leng - 1:
                return y
            for val in path[x]:
                if val not in seen:
                    deq.append((val, y+1))
                    seen.add(val)
        '''