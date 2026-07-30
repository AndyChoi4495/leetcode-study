class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ''' 
        
        sliding window

        add until include t string 
        using left pointer to remove from the begining until have the string 
        check the shortest length, 
        index
        '''

        count1 = {}
        count2 = {}
        if len(s) < len(t):
            return ""

        for c in t:
            count1[c] = 1 + count1.get(c, 0)

        resLen = float('inf')
        res = [-1, -1]
        need = len(count1)
        have = 0
        l = 0
        for r in range(len(s)):
            count2[s[r]] = 1 + count2.get(s[r], 0)

            if s[r] in count1 and count1[s[r]] == count2[s[r]]:
                have += 1
            
            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l , r]
                count2[s[l]] -= 1

                if s[l] in count1 and count1[s[l]] > count2[s[l]]:
                    have -= 1
                
                l += 1
        l , r = res

        return s[l:r+1]






            
        