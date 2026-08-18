class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        # {-4, -1, -1, 0, 1, 2}
        res = []
        for i, a in enumerate(nums):

            if a > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1


            while l < r:
                total = a + nums[l] + nums[r]

                if total == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
                
                
        return res

        