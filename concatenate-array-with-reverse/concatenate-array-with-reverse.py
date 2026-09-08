class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = []
        rev = nums[::-1]
        for i in nums:
            ans.append(i)

        for i in rev:
            ans.append(i)
            
        return ans
