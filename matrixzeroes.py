'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        m = len(matrix)
        n= len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                col0=0
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j]= matrix[i][0] = 0

        for i in reversed(range(m)):
            for j in reversed(range(1,n)):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if col0 == 0:
                matrix[i][0] =0

        return matrix


if __name__ == '__main__':
    print Solution().setZeroes([[1,1,1],[0,1,2]])
    print Solution().setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])