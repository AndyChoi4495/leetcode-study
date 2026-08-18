class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        ''' 
        O(n)
        O(n)
        
        '''
        hashSet = {}

        for i, a in enumerate(nums):
            if target - a in hashSet:
                return [hashSet[target - a ] ,i]
            hashSet[a] = i
        
        return []


        