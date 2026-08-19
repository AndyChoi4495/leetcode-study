class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []


        ''' 
        7 1 7 2 2 4

        if height is bigger than max so far

        pop() and cal
        
        '''

        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            startIdx = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                startIdx = idx
            stack.append((startIdx, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea