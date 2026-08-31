class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pair = 0
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                print(nums[i], nums[j])
                if nums[i] + nums[j] < target:
                    pair += 1
                
        return pair
