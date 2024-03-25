class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        rx = x[::-1]
        if x == rx:
            return True
        else:
            return False
