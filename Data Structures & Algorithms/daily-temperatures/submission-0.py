class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [] # store the indicies in monotinc seq
        res = [0] * n 
        for i in range(n):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res 


        