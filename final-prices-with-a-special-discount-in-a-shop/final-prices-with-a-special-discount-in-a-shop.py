class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        check = False

        for i in range(0, len(prices)):
            check = False
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    res.append(prices[i] - prices[j])
                    check = True
                    break
            if not check:
                res.append(prices[i])
        
        return res
