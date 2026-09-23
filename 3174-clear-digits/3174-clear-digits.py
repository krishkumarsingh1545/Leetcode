class Solution:
    def clearDigits(self, s: str) -> str:
        new = []
        for i in s:
            if i.isdigit():
                new.pop()
            else:
                new.append(i)
        return ''.join(new)