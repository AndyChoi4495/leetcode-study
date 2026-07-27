class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        ''' 
        if next number exist in nums array, + 1 else stop
        '''

        longest = 0
        numSet = set(nums)

        l = 0

        for r in range(len(nums)):

            if nums[r] - 1 not in numSet:
                length = 1
                while nums[r] + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

       


        
        