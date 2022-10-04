# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        leng = len(words)
        possible = [i for i in range(leng)]
        pair = [[0 for _ in range(leng)] for _ in range(leng)]
        for i in range(leng):
            for j in range(i, leng):
                cnt = 0
                for k in range(len(words[0])):
                    if words[i][k] == words[j][k]:
                        cnt += 1
                pair[i][j] = cnt
                pair[j][i] = cnt

        def cal(possible):
            if len(possible) == 1:
                return (possible[0], [])
            guess, res, min1 = -1, [], float('inf')
            for i in range(len(words)):
                list1 = [[] for _ in range(len(words[0]) + 1)]
                for j in possible:
                    list1[pair[i][j]].append(j)
                if len(max(list1, key=len)) < min1:
                    min1 = len(max(list1, key=len))
                    guess = i
                    res = list1
            return (guess, res)

        while possible:
            guess, list1 = cal(possible)
            match = master.guess(words[guess])
            if match == len(words[0]):
                return
            possible = list1[match]


