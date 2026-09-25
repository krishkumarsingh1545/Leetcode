class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        k = len(s)//2
        while k != 0:
            i = 0
            sub = s[:k]
            while i < len(s):
                if sub != s[i:k+i]:
                    break
                i += k
            if i == len(s):
                return True
            k -= 1
        return False
