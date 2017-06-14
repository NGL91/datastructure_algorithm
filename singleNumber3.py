#Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear #exactly twice. Find the two elements that appear only once.

#For example:

#Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
import operator

# a& -a = 
class Solution():
	def singleNumber3(self, lists):
		xor_a_b = reduce(operator.xor, lists)
		bit = xor_a_b & -xor_a_b
		print xor_a_b,bit
		result = [0, 0]
		for item in lists:
			result[bool(item & bit)] ^= item

		return result



if __name__ == '__main__':
	print Solution().singleNumber3([1, 2, 1, 3, 2, 5])