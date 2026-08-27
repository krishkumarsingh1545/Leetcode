class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        unique_sum = sum(set(nums))
        missing = len(nums) * (len(nums) + 1) // 2 - unique_sum
        
        return [sum(nums) - unique_sum, missing]