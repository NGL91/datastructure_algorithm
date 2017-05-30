# Time:  O(n)
# Space: O(1)
# 
# Given an array of integers, every element appears three times except for one appears two times. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution1:
	def twiceNumber(self, A):
		once = 0
		twice = 0
		for item in A:
			twice = item & once
			once = once ^ item
			three = once & twice 
			once = once  & ~ three
			twice  = twice & ~three
		print twice,once
		return twice |once

class Solution2:
	def twiceNumber(self, A):
		return sum(list(set(A))*3) - sum(A)

if __name__ == '__main__':
	print Solution1().twiceNumber([1,2,3,4,1,2,3,4,1,2,3,4,5,5,7,7,5])

	print Solution2().twiceNumber([1,2,3,4,1,2,3,4,1,2,3,4,5,5,7,7,5])
