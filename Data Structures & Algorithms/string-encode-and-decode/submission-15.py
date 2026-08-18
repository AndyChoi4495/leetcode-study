class Solution:

    def encode(self, strs: List[str]) -> str:

        ''' 
        Hello , World
        5#Hello5#World
        '''
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        
        return string



    def decode(self, s: str) -> List[str]:
        ''' 
        Hello , World
        5#Hello5#World
         r
          l
                r
        '''

        l = 0
        r = 0
        res = []
        while r < len(s):
            while s[r] != "#":
                r += 1

            length = int(s[l:r])
            l = r + 1
            r = l + length
            word = s[l:r]
            res.append(word)
            l = r
        return res
