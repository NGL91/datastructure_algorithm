#Given an integer, write a function to determine if it is a power of two.
import math
import time


#Running: 138ms
#How: only highest digit in true number is 1, so n & n-1 == 0
class Solution1():
	def powerOfTwo(self, a):
		if a< 1:
			return False
		return not(a & (a-1))

#Space: O(1)
#Running: 66ms
#how: only one ditgit in binary number (power of 2) is 1
class Solution2():
	def powerOfTwo(self, a):
		if a <1:
			return False

		len = int(math.log(a, 2))+1
		return (1 << len-1) == a




if __name__ == "__main__":
	
	print Solution2().powerOfTwo(15)
	