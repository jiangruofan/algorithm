class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        def transform(num):
            leng = 0
            s = []
            cnt = 0
            index = 0
            for _ in range(len(target)):
                if num & 1:
                    cnt += 1
                else:
                    if cnt:
                        s.append(str(cnt))
                        cnt = 0
                        leng += 1
                    s.append(target[index])
                    leng += 1
                index += 1
                num >>= 1
            if cnt:
                s.append(str(cnt))
                leng += 1
            return (leng, s)

        def check(s1, s2):
            leng = len(s1)
            index = 0
            for i in range(leng):
                if s1[i].isdigit():
                    index += int(s1[i])
                else:
                    if s1[i] != s2[index]:
                        return False
                    index += 1
            return True

        min1 = float('inf')
        res = ""
        for i in range(1 << len(target)):
            leng, s = transform(i)
            if leng >= min1:
                continue
            judge = False
            for j in range(len(dictionary)):
                if len(dictionary[j]) != len(target):
                    continue
                if check(s, dictionary[j]):
                    judge = True
                    break
            if not judge and leng < min1:
                min1 = leng
                res = s
        return "".join(res)

