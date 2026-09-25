class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        count = 0
        for i in grid:
            l = 0
            h = n - 1
            k = n
            while l <= h:
                mid = l + (h - l)//2
                if i[mid] < 0:
                    k = mid
                    h = mid - 1
                else:
                    l = mid + 1
            count += (n - k)
        return count
            
