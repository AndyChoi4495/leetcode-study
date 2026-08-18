class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ''' 
        hash set
        sliding window 
        O(N)
        O(N)
        
        '''

        window = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            longest = max(longest, len(window))
        
        return longest