class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ''' 
        
        two pointer 

        O(N)
        0(1)
         '''

        l = 0
        r = len(heights) - 1
        maxWater = 0

        while l < r:
            h = min(heights[l], heights[r])
            length = r - l 
            size = h * length
            maxWater = max(maxWater, size)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater
