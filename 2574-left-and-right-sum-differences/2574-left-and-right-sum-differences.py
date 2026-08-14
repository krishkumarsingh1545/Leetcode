class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        diffArr = []
        s = 0
        for i in nums:
            diffArr.append(s)
            s += i
        s = 0
        for i in range(len(nums) - 1, -1, -1):
            diffArr[i] = abs(diffArr[i] - s)
            s += nums[i]
        return diffArr