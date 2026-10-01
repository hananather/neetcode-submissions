class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"*" : lambda x,y: x*y,
                "+" : lambda x,y : x+y,
                "-" : lambda x, y: x - y,
                "/" : lambda x, y: x / y
        }

        stack = []
        n = len(tokens)
        i = 0
        while i < n:
            t = tokens[i]
            if t.isdigit():
                stack.append(t)
                i += 1
            if t in ops:
                y = int(stack.pop())
                x = int(stack.pop())
                res = ops[t](x, y)
                stack.append(res)
                i += 1
        return stack[0]
