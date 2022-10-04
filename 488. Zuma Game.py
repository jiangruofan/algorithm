class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = "".join(sorted(list(hand)))

        def remove(s):
            while 1:
                cnt = 1
                judge = False
                for i in range(1, len(s)):
                    if s[i] == s[i - 1]:
                        cnt += 1
                    else:
                        if cnt >= 3:
                            s = s[:i - cnt] + s[i:]
                            cnt = 1
                            judge = True
                            break
                        else:
                            cnt = 1
                if cnt >= 3:
                    s = s[:len(s) - cnt]
                    judge = True
                if not judge:
                    break
            return s

        deq = deque([(board, hand)])
        seen = set([board])
        res = 0
        while deq:
            for _ in range(len(deq)):
                x, y = deq.popleft()
                if not x:
                    return res
                for j, s in enumerate(y):
                    if j > 0 and s == y[j - 1]:
                        continue
                    for i in range(len(x)):
                        if i > 0 and s == x[i - 1]:
                            continue
                        if i > 0 and s != x[i] and s != x[i - 1] and x[i - 1] != x[i]:
                            continue
                        new = x[:i] + s + x[i:]
                        new = remove(new)
                        if new not in seen:
                            deq.append((new, y[:j] + y[j + 1:]))
                            seen.add(new)
            res += 1
        return -1

