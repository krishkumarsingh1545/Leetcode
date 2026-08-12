class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        sum = 0
        for i in range(len(nums)):
            if sum == 0: start = i

            sum += nums[i]

            if sum > max:
                max = sum
                arrStart = start
                arrEnd = i

            if sum < 0:
                sum = 0
        # print(arrStart, arrEnd)
        return max