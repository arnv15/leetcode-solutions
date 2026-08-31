class Solution:
    def maxFreqSum(self, s: str) -> int:
        og = [i for i in s]
        letters = list(set(i for i in s))
        vowels = ["a", "e", "i", "o", "u"]

        vc = 0
        cc = 0
        for letter in letters:
            count = og.count(letter)
            if (letter in vowels) and count > vc:
                vc = count
            if (letter not in vowels) and count > cc:
                cc = count
        return vc + cc
