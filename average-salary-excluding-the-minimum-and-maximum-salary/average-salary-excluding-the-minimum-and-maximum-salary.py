class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop(-1)
        ans = 0
        for i in salary:
            ans += i
        return ans/len(salary)
