class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        leftMax = height[0]
        rightMax = height[-1]

        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res