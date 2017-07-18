'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for item in nums:
            if item >= max1:
                if item > max1:
                    max3 =max2
                    max2 = max1
                    max1 = item
            elif item >= max2:
                if item > max2:
                    max3 = max2
                    max2=item
            elif item > max3: 
                max3 = item
            print max3, max2, max1
                
        if max3 > float('-inf'):
            return max3
        return max1

if __name__ == "__main__":
    print Solution().thirdMax([3,3,4,3,4,3,0,3,3])
