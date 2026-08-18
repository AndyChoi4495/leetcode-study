class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ''' 
        hashSet
        O(N)
        O(N)
        '''

        numSet = set(nums)
        longest = 0

        l = 0

        for r in range(len(nums)):

            if nums[r] - 1 not in numSet:
                length = 1
                while nums[r] + length in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest

