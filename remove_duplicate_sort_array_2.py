"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. 
It doesn't matter what you leave beyond the new length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0
            
        same = False
        temp = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[temp] or not same:
                same = nums[i] == nums[temp]
                nums[temp+1] = nums[i]
                temp +=1
                
        
        return temp+1



if __name__ =='__main__':
    print Solution().removeDuplicates([1,1,1,2,2,3])