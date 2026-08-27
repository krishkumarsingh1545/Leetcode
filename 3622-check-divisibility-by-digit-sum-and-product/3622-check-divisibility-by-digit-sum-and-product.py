class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, m = 1, n
        d = 0
        while m != 0:
            d += (m % 10)
            s *= (m % 10)
            m //= 10
        return n % (d + s) == 0