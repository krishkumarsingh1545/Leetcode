class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        hasharr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                        hasharr.append([i, j])
        for k in hasharr:
            for i in range(len(matrix[k[0]])):
                matrix[k[0]][i] = 0
            for i in range(len(matrix)):
                matrix[i][k[1]] = 0
        print(matrix)