class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashRansom = {}
        hashMag = {}
        for i in ransomNote:
            if i not in hashRansom:
                hashRansom[i] = 1
            else:
                hashRansom[i] += 1
        for i in magazine:
            if i not in hashMag:
                hashMag[i] = 1
            else:
                hashMag[i] += 1
        for key, value in hashRansom.items():
            if hashRansom.get(key) > hashMag.get(key, 0):
                return False
        return True
