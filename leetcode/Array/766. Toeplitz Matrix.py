# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        rowNum = len(matrix)
        colNum = len(matrix[0])
        
        for i in range(rowNum):
            for j in range(colNum):
                if i >= 1 and j >= 1:
                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
        return True