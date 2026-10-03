class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        out = ""

        for i in range(len(strs[0])):
            prefix = strs[0][i]

            for s in range(1, len(strs)):
                if i >= len(strs[s]) or strs[s][i] != prefix:
                    return out

            out += prefix

        return out