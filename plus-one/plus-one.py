class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = [str(i) for i in digits]
        res = str(int("".join(num)) + 1)
        return [int(i) for i in res]
