class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitToChar = {'1': '' , '2' : 'abc', '3': 'def',
         '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
          '8': 'tuv', '9' : 'wxyz', '0': '+'}


        res = []
        
        def dfs(i, subset):
            if len(subset) == len(digits):
                res.append("".join(subset))
                return
            cur_digit = digits[i]
            letters = digitToChar[cur_digit]

            for c in letters:
                subset.append(c)
                dfs(i+1,subset)
                subset.pop()
        dfs(0,[])

        return res if len(digits) > 0 else []
            