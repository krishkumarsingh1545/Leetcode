class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        j = len(s)
        for i in range(j):
            if goal == (s[i:] + s[:i]):
                return True
        return False