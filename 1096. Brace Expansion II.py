class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = [{""}]
        for s in expression:
            if s == "{":
                stack += [set(), {""}]
            elif s == "}":
                x = stack.pop() | stack.pop()
                stack[-1] = {val + val1 for val in stack[-1] for val1 in x}
            elif s == ",":
                stack[-2] |= stack[-1]
                stack[-1] = {""}
            else:
                stack[-1] = {val + s for val in stack[-1]}
        return sorted(list(stack[-1]))