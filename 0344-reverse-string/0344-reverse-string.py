class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        # for i in range(len(s)):
        #     s[i], s[len(s) -1 -i] = s[len(s) -1 -i], s[i]
        return s
