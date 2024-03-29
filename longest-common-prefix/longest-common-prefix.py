class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        first = sorted(strs)[0]
        last = sorted(strs)[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]: 
                return ans
            else: 
                ans += first[i]
        return ans
        
