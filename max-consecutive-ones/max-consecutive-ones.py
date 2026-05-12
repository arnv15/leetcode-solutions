class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        ans = 0
        for i in nums:
            if i == 0:
                curr = 0
            else:
                curr += 1
            
            if curr > ans:
                ans = curr
        return ans
            
        
