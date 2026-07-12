class Solution:
    def arraySign(self, nums: List[int]) -> int:
        chk = 0
        for i in nums:
            if i < 0:
                chk += 1
            if i == 0:
                return 0
        # print(chk)
        return 1 if chk % 2 == 0 else -1