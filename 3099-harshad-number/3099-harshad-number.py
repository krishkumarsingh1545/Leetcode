class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s, n = 0, x
        while n != 0:
            s += (n % 10)
            n //= 10
        return s if x % s == 0 else -1