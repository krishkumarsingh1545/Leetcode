class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for k in range(n // 2, 0, -1):
            if n % k != 0:
                continue

            sub = s[:k]

            if sub * (n // k) == s:
                return True

        return False