class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx = 0
        left = 0
        window = set()
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right])
            maxx = max(maxx, right- left + 1)
        return maxx