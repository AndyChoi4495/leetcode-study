class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 2,9,8,3,6 rob first house or rob last house

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(self.help(nums[1:]), self.help(nums[:-1])) 



    def help(self, arr):
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]

        n = len(arr)

        dp = [0] * n

        dp[0] = arr[0]
        dp[1] = max(arr[1], arr[0])

        for i in range(2,n):
            dp[i] = max(dp[i-2] + arr[i], dp[i-1])
        
        return dp[n-1]