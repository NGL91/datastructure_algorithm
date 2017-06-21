# Time:  O(n)
# Space: O(1)
#
# Given a sorted integer array without duplicates,
# return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7],
# return ["0->2","4->5","7"].
#
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i=0
        while i < len(nums):
            start = nums[i]
            while i < len(nums) -1 and nums[i+1] - nums[i] ==1:
                i+=1
            
            if start == nums[i]:
                res.append(str(nums[i]))
            else:
                res.append(str(start)+ '-->' + str(nums[i]))

            i+=1
        
        return res


if __name__ == '__main__':
    print Solution().summaryRanges([0,1,2,4,5,7])