class Solution:
    def scoreOfString(self, s: str) -> int:
        asc = [ord(c) for c in s]
        sum = 0
        for i in range(0, len(asc)-1):
            sum += abs(asc[i] - asc[i+1])
        return sum
