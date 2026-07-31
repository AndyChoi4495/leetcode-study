class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ''' 
        p , s

        car cannot pass another car a head

        p - 1, 4  -> target 10
        s - 3  2
        1 2 3 4 5 6 7 8 9 10

        a   b
              a b
                    ab  

        a - 1 + 3s => (10 - 1) / 3 => 3hrs
        b - 4 + 2s => (10 - 4) / 2 => 3hrs

        if a >= b. => one fleet
        '''

        stack = []
        pair = [(p , s) for p , s in zip(position, speed)]
        pair.sort(reverse=True)
        for p, s in pair:
            h = (target - p) / s
            if not stack or h > stack[-1]:
                stack.append(h)
        return len(stack)

