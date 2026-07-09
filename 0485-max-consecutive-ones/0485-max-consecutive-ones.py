class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        m = 0
        for i in nums:
            if i == 1:
                count+=1
                continue
            m = max(m, count)
            count = 0
        return max(m, count)
        