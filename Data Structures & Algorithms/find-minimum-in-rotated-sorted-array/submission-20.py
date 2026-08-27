class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        ''' 
        1 2 3 4 5 6

        3 4 5 6 1 2
              l   r
                m
              r
              m  
        1 2 3 4 5 6
        
         '''

        l = 0
        r = len(nums) - 1

        res = float('inf')

        while l <= r:
            # if array is sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return res
            
            
