class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        f = 0
        while f <= x:
            if f**2 > x:
                return f-1
            if f**2 == x:
                return f
            f += 1
            




    
