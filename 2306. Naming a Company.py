import string
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ideas = set(ideas)
        dic = defaultdict(lambda: Counter())
        for word in ideas:
            for s in string.ascii_lowercase:
                if s != word[0] and s + word[1:] not in ideas:
                    dic[word[0]][s] += 1
        res = 0
        for word in ideas:
            for s in string.ascii_lowercase:
                if s != word[0] and s + word[1:] not in ideas:
                    res += dic[s][word[0]]
        return res
