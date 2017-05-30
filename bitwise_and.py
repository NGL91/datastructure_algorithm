#Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, 
#inclusive.

#For example, given the range [5, 7], you should return 4.
import math
import operator
import functools

#Bad, can not overcome test case
class Solution1():
	def rangebitwise(self, m, n):
		res = n
		while n >m:
			n=n-1
			res &= n

		return res




#185ms
#space=O(1)
#Based on the fact that last bit of (odd number & even number) = 0
class Solution3():
	def rangebitwise(self, m, n):
		i = 1
		while m != n:
			 m >>= 1
			 n >>= 1
			 i <<= 1
		print 
		return i *m


#B108ms
#Based on the fact that the number of digit in a birary number = int(math.log(n,2))+1
class Solution2():
	def rangebitwise(self, m, n):
		if m == 0:
			return 0

		if m == n:
			return m

		if int(math.log(m,2)) < int(math.log(n,2)):
		#Mean that some where else in range have a number like 1xxxx , x is 0. and a number like 0anvv
			return 0

		return functools.reduce(operator.and_,range(m, n+1) )


if __name__ == '__main__':
	print Solution3().rangebitwise(25,28)

