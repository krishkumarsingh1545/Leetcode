class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        outs = []
        fixed = 0
        while (fixed < len(nums) - 2):
            left = fixed + 1
            right = len(nums) - 1
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                fixed += 1
                continue
            while left < right:
                total = nums[fixed] + nums[left] + nums[right]
                if total == 0:
                    outs.append([nums[fixed], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
            fixed += 1

        return outs