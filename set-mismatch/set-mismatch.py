class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        missing = -1
        for n in range(1, len(nums)+1):
            count = nums.count(n)
            if count == 0:
                missing = n

            if count == 2:
                dup = n
        return [dup, missing]
