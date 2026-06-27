class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = {}
        temp = n

        while temp != 0:
            d = temp % 10
            if d not in freq:
                freq[d] = 1
            else:
                freq[d] += 1
            temp //= 10

        score = 0
        for key, value in freq.items():
            # print(key, value)
            score += key * value

        return score