class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        '''
        7, 4 ,1, 0

        10 - 7 = 3 / 1 => 3
        10 - 4 = 6 / 2 => 3  combine one 
        '''

        pair = [(p, s) for p,s in zip(position, speed)]

        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            time = (target - p) / s
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        return len(stack)

            
