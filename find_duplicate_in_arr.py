# -*- coding: utf-8 -*-

'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for index in xrange(len(nums)):
            
            while nums[index] != index+1 and nums[index] != 0:
                # print index,  nums[index],nums[index]-1
                if nums[index] ==  nums[nums[index]-1] :
                    print res, nums, index
                    res.append(nums[index])
                    nums[index] = 0
                    print res, nums, index
                else:
                    temp = nums[index]
                    nums[index] = nums[temp-1]
                    nums[temp-1] = temp

        
        return list(set(res))

if __name__ == '__main__':
    print Solution().findDuplicates([4,3,2,7,8,2,3,1])