class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        ans = -1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] >= target:
                if nums[mid] == target:
                    ans = mid
                r = mid - 1
            else:
                l = mid + 1
        if ans == -1: return [-1, -1]
        ans2 = ans
        l, r = ans, len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] <= target:
                if nums[mid] == target:
                    ans2 = mid
                l = mid + 1
            else:
                r = mid - 1
        return [ans, ans2]