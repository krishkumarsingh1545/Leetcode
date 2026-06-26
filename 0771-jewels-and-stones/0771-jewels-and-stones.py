class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        store = {}
        sum = 0
        for i in stones:
            if i not in store:
                store[i] = 1
            else:
                store[i]+=1
        for i in jewels:
            sum += store.get(i, 0)
        return sum