class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        avg = s/k
        for i in range(len(nums) - k):
            s = s - nums[i] + nums[i+k]
            avg = max(avg, s/k)
        return avg