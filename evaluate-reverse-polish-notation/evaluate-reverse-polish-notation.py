class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        res = []
        for num in tokens:
            if num not in ops:
                res.append(num)
            else:
                n2 = res.pop()
                n1 = res.pop()
                if num == "+":
                    res.append(int(n1) + int(n2))
                elif num == "-":
                    res.append(int(n1) - int(n2))
                elif num == "*":
                    res.append(int(n1) * int(n2))
                else:
                    res.append(int(n1) / int(n2))
        return int(res[0])
