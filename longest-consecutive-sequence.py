# Time:  O(n)
# Space: O(n)
#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# 
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# 
# Your algorithm should run in O(n) complexity.
#


#Idea is let check if number is start of a sequence and test to find out the biggest element in sequence
class Solution():
	def longestConsecutive(self, lists):
		results = 0
		nums = set(lists)
		for i in nums:
			if i-1 not in nums:
				y = i
				while y in nums:
					y+=1
				results = max(results, y-i)

		return results


	#Faster
'''Whenever a new element n is inserted into the map, do two things:

See if n - 1 and n + 1 exist in the map, and if so, it means there is an existing sequence next to n. Variables left and right will be the length of those two sequences, while 0 means there is no sequence and n will be the boundary point later. Store (left + right + 1) as the associated value to key n into the map.
Use left and right to locate the other end of the sequences to the left and right of n respectively, and replace the value with the new length.class Solution2():
'''
class Solution2():
	def longestConsecutive(self, num):
		if len(num) == 0:
			return 0
		result, lengths = 1, {key: 0 for key in num}
		for i in num:
			if lengths[i] == 0:
				lengths[i] = 1
				left, right = lengths.get(i - 1, 0), lengths.get(i + 1, 0)
				length = 1 + left + right
				result, lengths[i - left], lengths[i + right] = max(result, length), length, length
		return result


# class Solution3():
# 	def longestConsecutive(self, nums):
# 		r = 0
# 		lengths = {}
# 		for i in nums:
# 			lengths[i] = lengths[i+ length[i+1]] = lengths[i + length[i-1]] = lengths[i+1] + lengths[i-1] + 1
# 			r = max(r, lengths[i] )

# 		return r


if __name__ == "__main__":
    print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])

    print Solution2().longestConsecutive([1])

    print Solution3().longestConsecutive([1])