"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

ex: [1,2,3,6] ===> [1,2,3,7]
	[1,2,8,9] === > [1,2,9,0]

"""

#idea: convert to number to plus 1, then convert to str and array
#42ms
class Solution():
	def plusOne1(self, digits):
		digits = [str(x) for x in digits]
		digits = ''.join(digits)
		return [int(item) for item in str(int(digits)+1)]

	def plusOne(self, digits):
		num = 0
		for i in range(len(digits)):
			num = num*10 + digits[i]

		return [int(i) for i in str(num+1)]

#idea: loop from last to add 1
#39ms
class Solution2():
	def plusOne(self, digits):
		for i in reversed(range(len(digits))):
			if digits[i] <9:
				digits[i] +=1
				return digits

			digits[i] = 0

		res = [1]
		res.extend(digits)
		return res

if __name__ == '__main__':
	print Solution().plusOne1([1,4,7,9])
	print Solution().plusOne([1,0])

	print Solution2().plusOne([9,9,9,9])
	print Solution2().plusOne([1,0])