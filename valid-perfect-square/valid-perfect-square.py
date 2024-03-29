class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sqrt = str(num**0.5)
        if sqrt[-1] == "0":
            return True
        else:
            return False
