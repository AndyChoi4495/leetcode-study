class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointer

        res = ""
        resLen = 0


        # odd

        for i in range(len(s)):

            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < len(s[l:r+1]):
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        # even
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < len(s[l:r+1]):
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1
            
        return res
            
