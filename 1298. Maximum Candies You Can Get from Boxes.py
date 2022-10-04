class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        res = 0
        deq = deque(initialBoxes)
        key = set()
        unopened = set()
        while deq:
            leng = len(deq)
            for _ in range(leng):
                x = deq.popleft()
                res += candies[x]
                key.update(keys[x])
                for val in containedBoxes[x]:
                    if status[val]:
                        deq.append(val)
                    else:
                        unopened.add(val)
            for val in set(unopened):
                if val in key:
                    deq.append(val)
                    key.remove(val)
                    unopened.remove(val)
        return res
