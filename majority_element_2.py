# -*- coding: utf-8 -*-
'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
            
        candidate1, count1, candidate2, count2 = nums[0], 0, nums[0], 0
        for item in nums:
            if item == candidate1:
                count1 +=1
            elif item == candidate2:
                count2 +=1
            elif count1 ==0:
                candidate1 = item
                count1 = 1
            elif count2 == 0:
                candidate2 = item
                count2 = 1
            
            
            else:
                count1 -=1
                count2 -=1
        print candidate1, candidate2
        return [n for n in set([candidate1, candidate2])
                    if nums.count(n) > len(nums) // 3]


if __name__ == '__main__':
    print Solution().majorityElement([8,8,7,7,7])