class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            count = 1
            for i in range(len(digits) - 1, -1, -1):
                if count == 1 and digits[i] != 9:
                    digits[i] += 1
                    count = 0
                if digits[i] == 9 and count == 1:
                    digits[i] = 0
                    count = 1
            if i == 0 and count == 1:
                digits.insert(0, 1)
        return digits
            