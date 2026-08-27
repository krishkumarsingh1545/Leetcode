class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hash = sorted(nums)
        return [hash.index(i) for i in nums]
        