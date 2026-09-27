class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def both_occurence(is_left):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = left + (right - left)//2

                if nums[mid] == target:
                    result = mid
                    if is_left:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return result
        return [both_occurence(True), both_occurence(False)]