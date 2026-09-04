class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            maxval = minval = nums[i]
            for j in range(i):
                maxval = max(maxval, nums[j])
            for j in range(i+1, n):
                minval = min(minval, nums[j])
            if maxval - minval <= k:
                return i
        return -1
