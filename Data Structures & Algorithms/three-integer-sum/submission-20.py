class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ''' 
        Sort the array to avoid the duplicated value
        loop the array, but if first value is bigger than 0, total sum cannot be 
        0. 

        '''
 
        nums.sort()
        res = []
        # -4, -1, -1, 0, 1, 2
        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

            
