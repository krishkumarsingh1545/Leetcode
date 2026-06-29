class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one = m - 1
        two = 0
        while one >= 0 and two < n:
            if nums1[one] > nums2[two]:
                nums1[one], nums2[two] = nums2[two], nums1[one]
                one-=1
                two+=1
            else:
                break
        nums1[:] = nums1[:m]
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()
        # nums2.sort()