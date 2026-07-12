class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        num1, num2 = 0, 0
        for i in nums:
            num1 += i
            if i > 9:
                k = i
                while k != 0:
                    num2 += (k % 10)
                    k //= 10
            else:
                num2 += i
        return abs(num1 - num2)