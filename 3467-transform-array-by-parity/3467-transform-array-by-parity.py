class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        e, o = 0, 0
        for i in range(len(nums)):
            if nums[i] % 2:
                o += 1
            else:
                e += 1
        
        for i in range(e):
            nums[i] = 0
        for i in range(e, e+o):
            nums[i] = 1
        return nums