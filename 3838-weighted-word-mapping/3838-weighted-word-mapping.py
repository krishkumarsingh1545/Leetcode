class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ret = ""
        for i in words:
            ind = 0
            for j in i:
                ind += weights[ord(j) - ord('a')]
            ind = ind % 26
            ret += chr(ord('z') - ind)
        return ret