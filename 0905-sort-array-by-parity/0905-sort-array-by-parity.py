class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow = 0
        # for slow in range(0, len(nums)):
        #     if nums[slow]%2 != 0:
        #         continue
        for fast in range(1, len(nums)):
            if nums[slow]%2 == 0:
                slow+=1
                continue
            if nums[fast]%2 == 0 and slow < fast:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow+=1
        return nums