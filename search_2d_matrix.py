'''Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''

#Start from right top corner
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or len(matrix) <1 or len(matrix[0]) <1:
            return False
        
        col = len(matrix[0])-1
        row = 0
        max_row = len(matrix)-1
        while col >=0 and row <= max_row:
			print row, col
			if matrix[row][col] == target:
				return True
			elif target < matrix[row][col]:
				col -=1
			else:
				row +=1
        
        return False


a=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

if __name__ == '__main__':
    print Solution().searchMatrix(a,5)
