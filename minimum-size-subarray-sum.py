# -*- coding: utf-8 -*-

# Time:  O(n)
# Space: O(1)
#
# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        sum = 0
        min_size = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
            	min_size = min(min_size, i-start+1)
                sum -= nums[start]
                start+=1
            
        
        return min_size if min_size != float('inf') else 0
                
        
        
if __name__ == '__main__':
	print Solution().minSubArrayLen(11, [1,2,3,4,5])

