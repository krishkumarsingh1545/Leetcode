class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ''
        k = min(len(word1), len(word2))
        for i in range(k):
            new += (word1[i] + word2[i])
        # print(new)
        new += word1[k:]
        new += word2[k:]
        return new