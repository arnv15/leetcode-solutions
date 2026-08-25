class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        itr = k
        while len(nums) > 0:
            if itr in nums:
                nums.remove(itr)
            else:
                return itr
            itr += k 
        return itr
