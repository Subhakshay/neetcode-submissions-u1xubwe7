class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        for c in range(0,len(temperatures)):
            warmer = False
            for i in range(c,len(temperatures)):
                if temperatures[c] < temperatures[i]:
                    stack.append(i-c)
                    warmer = True
                    break
            if not warmer:
                stack.append(0)
        return stack
            
