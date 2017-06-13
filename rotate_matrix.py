#You are given an n x n 2D matrix representing an image.

#Rotate the image by 90 degrees (clockwise).


class Solution():

	#beat 50%
	def rotate(self, matrix):
		'''
		 * clockwise rotate
		 * first reverse up to down, then swap the symmetry 
		 * 1 2 3     7 8 9     7 4 1
		 * 4 5 6  => 4 5 6  => 8 5 2
		 * 7 8 9     1 2 3     9 6 3
		'''
		matrix.reverse()
		for i in range(len(matrix)):
			for j in range(i):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


	def anti_rotate(self, matrix):
		'''
				
		 * anticlockwise rotate
		 * first reverse left to right, then swap the symmetry
		 * 1 2 3     3 2 1     3 6 9
		 * 4 5 6  => 6 5 4  => 2 5 8
		 * 7 8 9     9 8 7     1 4 7
		*/
		'''
		[item.reverse() for item in matrix]
		for i in range(len(matrix)):
			for j in range(i):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



	#Beat 98%
	#44ms
	def rotate1(self, matrix):
		#matrix[::-1] to reverse up to down
		#zip to transpose
		matrix[:] = zip(*matrix[::-1])

if __name__ == '__main__':
	print Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])