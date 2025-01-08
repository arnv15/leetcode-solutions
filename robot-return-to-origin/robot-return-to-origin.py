class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        for i in moves:
            if i == "L":
                pos[0] -= 1

            elif i == "R":
                pos[0] += 1

            elif i == "U":
                pos[1] += 1
            
            else:
                pos[1] -=1
        
        return pos == [0, 0]
