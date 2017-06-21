# Time:  O(n)
# Space: O(1)
#
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than [n/2] times.
# 
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1
        
        for i in xrange(1, len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1

            # print i, cnt, idx
        
        return nums[idx]


#run failed with minus number
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        major = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(31):
            bit_count = 0
            mask = 1 << i
            for idx, a in enumerate(nums):
                # print idx, a, mask
                if a & mask:
                    bit_count +=1
                # print bit_count, idx, a,
                if bit_count > n/2:
                    major |= mask
                    # print 'break bit count', major
                    break
        
        return major


#Boyer moore agolrithm
class Solution3(object):
    def majorityElement(self, nums):
        count = 0
        candidate = 0
        for item in nums:
            if count == 0:
                candidate = item
            if item == candidate:
                count +=1
            else:
                count -=1

        return candidate
    
        

if __name__ == "__main__":
    print Solution().majorityElement([1,1,2,2,1])

    print Solution2().majorityElement([-1,-1,2147483647])

    print Solution3().majorityElement([5, 5, 0, 0, 0, 5, 0, 0, 5])