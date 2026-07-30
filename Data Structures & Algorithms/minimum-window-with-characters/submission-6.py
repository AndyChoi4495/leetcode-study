class Solution:
    def minWindow(self, s: str, t: str) -> str:

        cnt1 = {}
        cnt2 = {}

        if len(s) < len(t) or s == "":
            return ""
        
        for c in t:
            cnt1[c] = 1 + cnt1.get(c, 0) 

        minLen = float('inf')
        res = [-1, -1]
        need = len(cnt1)
        l = 0
        have = 0
        for r in range(len(s)):
            cnt2[s[r]] = 1 + cnt2.get(s[r], 0)

            if cnt1.get(s[r], 0) == cnt2[s[r]]:
                have += 1
            
            while need == have:
                if minLen > r - l + 1:
                    minLen = r - l + 1
                    res = [l , r]
                cnt2[s[l]] -= 1

                if cnt1.get(s[l], 0) > cnt2[s[l]]:
                    have -= 1
                
                l += 1
        l, r = res
        return s[l:r + 1]