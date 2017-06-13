# Time:  O(n)
# Space: O(1)
#
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# For example,
# Given input array A = [1,1,2],
# 
# Your function should return length = 2, and A is now [1,2].
#

class Solution():
	def removeDuplicates(self, arr):
		if len(arr) == 0:
			return 0

		last, i = 0, 1
		while i< len(arr):
			if arr[i]!= arr[last]:
				last += 1
				arr[last] = arr[i]

			i+=1

		print arr
		return last+1






if __name__ == "__main__":
    print Solution().removeDuplicates([1, 1, 2, 3, 4, 4, 6])