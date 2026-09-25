class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        if s == '': return True
        for r in t:
            if s[l] == r:
                l += 1
            if l == len(s):
                return True
        return False