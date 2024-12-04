class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if (high % 2 == 0 and low % 2 == 0):
            return int((high-low) // 2)

        elif (high % 2 != 0 and low % 2 != 0):
            return int(((high-low) + 2) // 2)

        else:
            return int(((high-low) + 1) // 2)
