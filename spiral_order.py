#Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

#For example,
#Given the following matrix:

#[
 #[ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
#]
#You should return [1,2,3,6,9,8,7,4,5].

#45ms
class Solution():
	def spiral_order(self, matrix):
		res = []
		if matrix == []:
            return res
		u = 0
		d = len(matrix)-1
		l=0
		r=len(matrix[0])-1
		while True:
			#up col
			for col in range(l, r+1):
				res.append(matrix[u][col])
			u+=1
			if u > d:
				break
			#up row
			for row in range(u, d+1):
				res.append(matrix[row][r])
			r-=1
			if r<l:
				break
			#down col
			col_range = range(l, r+1)
			col_range.reverse()
			for col in col_range:
				res.append(matrix[d][col])
			d-=1
			if u > d:
				break
			#down row
			row_range = range(u, d+1)
			row_range.reverse()
			for row in row_range:
				res.append(matrix[row][l])

			l +=1
			if r<l:
				break
		return res

class Solution1():
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if matrix == []:
            return result
        
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        
        while left <= right and top <= bottom:
            for j in xrange(left, right + 1):
                result.append(matrix[top][j])
            for i in xrange(top + 1, bottom):
                result.append(matrix[i][right])
            for j in reversed(xrange(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(xrange(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
            
        return result

#39ms
class Solution2():
	def spiralOrder(self, matrix):
		res = []
		while matrix:
			res+= matrix.pop(0)
			if matrix and matrix[0]:
				for row in matrix:
					res.append(row.pop())

			if matrix:
				res += matrix.pop()[::-1]
			if matrix and matrix[0]:
				for row in matrix[::-1]:
					res.append(row.pop(0))

		return res


if __name__ == '__main__':
	print Solution().spiral_order([[1,2,3],[4,5,6],[7,8,9]])