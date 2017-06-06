class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        for j in range(0,len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1

        return i+1


#Faster, better
class Solution2():
    def removeElement(self, nums, val):
        i, last=0, len(nums)-1

        while i<= last:
            if nums[i] == val:
                nums[i], nums[last]=nums[last], nums[i]
                last -=1
            else:
                i+=1

        return last+1



if __name__ == "__main__":
    import time
    time1=time.time()
    print Solution().removeElement([1, 1, 2, 3, 4, 4, 6], 1)
    print 'time=',time.time()-time1


    time1=time.time()
    print Solution2().removeElement([1, 1, 2, 3, 4, 4, 6], 1)
    print 'time=',time.time()-time1