# -*- coding: utf-8 -*-

"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k, m
such that arr[i] < arr[j] < arr[k] < arr[m] given 0 ≤ i < j < k < m ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""

#Save the min at c1, and min except c1 at c2
class Solution(object):
    def increasingFour(self, nums):
        c1 = float('inf')
        c2 = float('inf')
        c3 = float('inf')
        for item in nums:
            if item <= c1:
                c1 = item
            elif item <= c2:
                c2 = item
            else:
                return True 
        return False
        


if __name__ == '__main__':
	print Solution().increasingFour([2,1,5,0,4,7])