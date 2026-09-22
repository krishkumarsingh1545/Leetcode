class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        s = s.split(sep=':')
        a, b = int(s[0][-1]), int(s[1][-1])
        u, v = s[0][0], s[1][0]
        kit = []
        for i in range(ord(u), ord(v)+1):
            for j in range(a, b+1):
                kit.append(chr(i) + str(j))
        return kit
