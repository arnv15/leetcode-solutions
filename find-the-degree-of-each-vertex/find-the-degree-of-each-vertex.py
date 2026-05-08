class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        vertix = []
        for vertice in matrix:
            vertix.append(sum(vertice))
        
        return vertix
        
