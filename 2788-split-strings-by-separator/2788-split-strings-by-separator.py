class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        k = len(words)
        for i in range(k):
            words.extend(words[i].split(sep = separator))
        return [x for x in words[k:] if x != ""]