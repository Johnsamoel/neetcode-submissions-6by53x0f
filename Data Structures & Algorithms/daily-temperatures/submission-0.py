class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, originalIndex = stack.pop()
                res[originalIndex] = (i - originalIndex)
            
            stack.append([t, i])
        
        return res