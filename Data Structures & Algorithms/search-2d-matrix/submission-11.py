class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ''' 
        
        binary search 
        each row is sorted

        '''

        top = 0
        btm = len(matrix) - 1

        while top <= btm:

            row = (top + btm) // 2

            if target < matrix[row][0]:
                btm = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        if not (top <= btm):
            return False
        row = (top + btm) // 2

        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1

        return False 

