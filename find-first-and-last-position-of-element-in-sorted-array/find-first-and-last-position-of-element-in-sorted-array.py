class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(nums, target, search):
            left = 0
            right = len(nums) - 1
            ind = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                
                elif nums[mid] > target:
                    right = mid - 1
                
                else:
                    ind = mid
                    if search:
                        right = mid - 1
                    else:
                        left = mid + 1
            return ind

        left = binary(nums, target, True)
        right = binary(nums, target, False)

        return [left, right]
