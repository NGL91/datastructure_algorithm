#Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

#For example,
#Given n = 3,

#You should return the following matrix:
#[
# [ 1, 2, 3 ],
# [ 8, 9, 4 ],
# [ 7, 6, 5 ]
#]

class Solution():

	#trick
	#		9 -- > 8 9    --->  6 7		-->    4 5   --->   1 2 3  
	#							9 8			   9 6			8 9 4
	#										   8 7			7 6	5
	#

	#44ms
	def generateMatrix(self, n):
		lo = n*n+1
		a=[]
		while lo >1:
			lo, hi = lo-len(a), lo
			a = [range(lo, hi)] + zip(*a[::-1])

		return a


class Solution2():
	#66ms
	def generateMatrix(self, n):
		a=[[0 for i in range(n)] for i in range(n)]
		start_row=0
		end_row=n-1
		start_col=0
		end_col=n-1
		k=1
		while start_col<= end_col and start_row <= end_row:
			for i in range(start_col, end_col+1):
				a[start_row][i] = k
				k+=1
			start_row+=1
			if start_row >end_row:
				break

			for i in range(start_row, end_row+1):
				a[i][end_col] = k
				k+=1
			end_col -=1
			if start_col >end_col:
				break

			for i in reversed(range(start_col, end_col+1)):
				a[end_row][i] = k
				k+=1
			end_row -=1

			if start_row >end_row:
				break


			for i in reversed(range(start_row, end_row+1)):
				a[i][start_col] = k
				k+=1
			start_col +=1

			if start_col >end_col:
				break

		return a


if __name__ == '__main__':

	print Solution().generateMatrix(4)


	print Solution2().generateMatrix(4)