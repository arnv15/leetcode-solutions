class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            count = 0
            for i in nums:
                if i < num:
                    count += 1
            ans.append(count)
        return ans
