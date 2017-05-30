#Reverse bits of a given 32 bits unsigned integer.

#For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
#return 964176192 (represented in binary as 00111001011110000010100101000000).
#time: O(32)
#Space: O(1)

class Solution:
	def reverse(self, a):
		res = 0
		for i in range(32):
			temp = ((a>> (31-i) ) &1) * 2**i
			res += temp

		return res


if __name__ == '__main__':
	print Solution().reverse(43261596)