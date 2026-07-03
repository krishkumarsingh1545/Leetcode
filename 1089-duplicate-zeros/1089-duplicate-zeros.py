class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        slow = 0
        while slow < len(arr) - 1:
            if arr[slow] == 0:
                temp = arr[slow+1]
                for fast in range(slow+1, len(arr)):
                    arr[fast], temp = temp, arr[fast]
                arr[slow+1] = 0
                slow+=1
            slow+=1
                    