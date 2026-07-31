class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # add index and temp (index, temp)
        res = [0] * len(temperatures)

        for i , t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                index , temp = stack.pop()
                days = i - index
                res[index] = days

            stack.append((i,t))

        return res
                
        ''' time complexity - O(N)
            space - O (N) '''