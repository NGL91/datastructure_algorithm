#Write a function that takes an unsigned integer and returns the number of 1 bits it has 
#(also known as the Hamming weight).

#For example, the 32-bit integer 11 has binary representation 00000000000000000000000000001011, 
#so the function should return 3.


class Solution:
	def number1bit(self, n):
		res = 0
		for i in range(32):
			res += ( (n >>i) &1 )
			# n = n >>1

		return res

class Solution2:
	def number1bit(self, n):
		res = 0
		while (n!=0):
			if n&1 == 1:
				res +=1
			n >>=1
		return res

#fastest
class Solution3:
	def number1bit(self, n):
        """
        hammingWeight
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result

if __name__ == '__main__':
	print Solution().number1bit(121)