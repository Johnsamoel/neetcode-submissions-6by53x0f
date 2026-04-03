class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #pairs [temp, index]
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack and stack[-1][0] > temperatures[i]:
                res[i] = (stack[-1][1] - i) 
            stack.append([temperatures[i], i])


        return res
