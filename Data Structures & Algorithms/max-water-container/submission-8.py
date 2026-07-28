class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ''' 
        two pointer 
        '''
        maxArea = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            h = min(heights[l], heights[r])
            area = (r - l) * h
            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea

