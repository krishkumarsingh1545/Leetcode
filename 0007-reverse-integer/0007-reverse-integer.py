class Solution:
    def reverse(self, x: int) -> int:

        sign: int = 1 if x > 0 else -1
        x = abs(x)

        if x > 2**31 - 1: return 0

        n: int = 0
        while x != 0:
            n = (n * 10) + (x % 10)
            x //= 10

        n *= sign

        if n < -(2**31) or n > 2**31 - 1:
            return 0
        return n