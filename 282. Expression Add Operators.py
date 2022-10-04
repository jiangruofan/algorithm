class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)
        def dfs(index, total, path, pre_num, pre_op):
            if index == n:
                if total == target:
                    res.append(path[1:])
                return
            for i in range(index, n):
                x = num[index:i+1]
                dfs(i+1, total + int(x), path+"+"+x, int(x), "+")
                if index != 0:
                    dfs(i+1, total - int(x), path+"-"+x, int(x), "-")
                if pre_op == "+":
                    dfs(i+1, total - pre_num + pre_num * int(x), path+"*"+x, pre_num*int(x), pre_op)
                elif pre_op == "-":
                    dfs(i+1, total + pre_num - pre_num * int(x), path+"*"+x, pre_num*int(x), pre_op)
                if num[index] == "0":
                    return
        dfs(0, 0, "", 0, "?")
        return res
