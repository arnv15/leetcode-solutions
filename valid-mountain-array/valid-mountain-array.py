from itertools import pairwise

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        def inc(lst):
            return all(x < y for x, y in pairwise(lst))

        def dec(lst):
            return all(x > y for x, y in pairwise(lst))

        num = max(arr)
        ind = arr.index(num)

        l1 = arr[:ind]
        l2 = arr[ind:]

        if ind == 0 or ind == len(arr) - 1:
            return False

        if inc(l1) and dec(l2):
            return True
        else:
            return False
        
