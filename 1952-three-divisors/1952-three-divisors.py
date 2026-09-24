class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        root = int(n ** 0.5)

        if root * root != n:
            return False

        for i in range(2, root):
            if root % i == 0:
                return False

        return True