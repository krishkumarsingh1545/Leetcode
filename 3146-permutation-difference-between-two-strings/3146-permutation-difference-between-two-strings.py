class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        k = 0
        for i in range(len(s)):
            k += abs(i - t.index(s[i]))
        return k