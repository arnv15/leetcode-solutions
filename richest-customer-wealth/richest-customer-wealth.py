class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0
        for lst in accounts:
            ltot = 0
            for num in lst:
                ltot += num
            if ltot > total:
                total = ltot
        return total
                
