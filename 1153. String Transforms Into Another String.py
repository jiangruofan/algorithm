class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if len(set(str2)) == 26:
            return str1 == str2

        str1 = list(str1)
        str2 = list(str2)

        dic1 = defaultdict(list)
        for i, val in enumerate(str1):
            dic1[val].append(i)

        for list1 in dic1.values():
            for i in range(1, len(list1)):
                if str2[list1[i]] != str2[list1[0]]:
                    return False

        return True


'''
a b c    a # c     b # c    b # a 
b c a    b c a     b c a    b c a

'''