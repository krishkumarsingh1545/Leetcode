class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        for i in range(1, len(nums)+1):
            if n % i == 0:
                # print(nums[i-1])
                s += nums[i-1]**2
        return s