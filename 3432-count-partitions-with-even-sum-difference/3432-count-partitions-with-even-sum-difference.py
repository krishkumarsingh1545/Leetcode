class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c = 0
        l, r = nums[0], sum(nums) - nums[0]
        for i in range(1, len(nums)):
            if (l - r) % 2 == 0: c += 1
            print(l - r)
            l += nums[i]
            r -= nums[i]
        return c