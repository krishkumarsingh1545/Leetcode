class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        if nums[0] == 0: return 0
        for i in range(1, len(nums)):
            s = 0
            while nums[i] != 0:
                s += (nums[i] % 10)
                nums[i] //= 10
            if s == i: return i
        return -1
