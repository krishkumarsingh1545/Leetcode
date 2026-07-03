class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        fixed = 0
        close = nums[0] + nums[1] + nums[2]
        for fixed in range(len(nums) - 2):
            # if nums[fixed] == nums[fixed-1]: continue
            left = fixed + 1
            right = len(nums) - 1
            while left < right:
                total = nums[fixed] + nums[left] + nums[right]
                if abs(total - target) < abs(close - target):
                    close = total
                if total == target:
                    return target
                elif total > target:
                    right-=1
                else:
                    left+=1
        return close