class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or s == "":
            return ""

        cntT = {}
        cntS = {}
        
        for c in t:
            cntT[c] = 1 + cntT.get(c, 0)

        need = len(cntT)
        have = 0
        minLen = float('inf')
        l = 0
        res = [-1, -1]
        
        for r in range(len(s)):
            cntS[s[r]] = 1 + cntS.get(s[r], 0)

            if cntT.get(s[r], 0) == cntS[s[r]]:
                have += 1
            while have == need:
                if minLen > r - l + 1:
                    minLen = r - l + 1
                    res = [l , r]
                cntS[s[l]] -= 1

                if cntS[s[l]] < cntT.get(s[l], 0):
                    have -= 1
                l += 1
        l , r = res
        return s[l:r+1]





            

            



        

        

        
        