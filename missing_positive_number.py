"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space O(1)
"""


class Solution(object):

    def firstMissingPositive(self, nums):
        """
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
             the range [1,...,l+1] 
        """
        nums.append(0)
        n=len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        
        
        for i in range(n):
            nums[nums[i]%n] += n
        
        for i in range(1,n):
            if nums[i]/n ==0:
                return i
        
        return n

    #Faster
    def firstMissingPositive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i< len(nums):
            if nums[i] >0 and nums[i]  <= len(nums) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i +=1
        
        print 'nums=',nums
        for i, integer in enumerate(nums):
            if integer != i+1:
                return i+1
        
        return len(nums) +1
        
    
    
        
        
        
if __name__ == '__main__':
    # print Solution().firstMissingPositive([3,4,-1,1])

    print Solution().firstMissingPositive1([0,4,1,2])