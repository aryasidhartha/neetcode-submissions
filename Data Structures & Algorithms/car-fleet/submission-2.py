class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        stack = []
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            
            # If the current car reaches the target in <= time than the fleet ahead,
            # it merges into that fleet (pop the faster time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)