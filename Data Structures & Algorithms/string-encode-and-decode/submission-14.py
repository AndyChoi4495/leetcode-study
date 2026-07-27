class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        # 5#Hello4#pear
        res = []
        l = 0
        r = 0
        while r < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            res.append(s[l:r])

            l = r
        return res
            


