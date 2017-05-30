# Time:  O(n)
# Space: O(1)
# 
# Given an array of integers, every element appears three times except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
import collections
import time

#space = O(n)
#Use space for dictionary
class Solution1:
	def singleNumber(self, A):
		print 'Solution1'
		res = {}
		for item in A:
			if res.get(item): 
				if res[item] == 2:
					del res[item]
				else:
					res[item] +=1
			else:
				res[item] = 1

		return res.keys()[0]




#Base on the fact that special item only appear 1 time, while others is 3
class Solution2:
	def singleNumber(self, A):
		print 'Solution2'
		return (sum(set(A))*3 - sum(A))/2

#Base on Counter
class Solution3:
	def singleNumber(self, A):
		print 'Solution3'
		return (collections.Counter(list(set(A))*3) - collections.Counter(A)).keys()[0]

#space = O(32)
#Base on the fact that integer number take 32 bit
class Solution4:
	def singleNumber(self, A):
		print 'Solution4'
		counter = []
		res = 0
		for i in range(0, 32):
			counter.append(0)
			for item in A:
				if (item >> i) &1:
					counter[i]  += 1

			counter[i] = counter[i] %3

			res += (counter[i] <<i)

		return res

#space = O(3)
#use var to count number of times bit appear
class Solution5:
	def singleNumber(self, A):
		print 'Solution5'
		once = 0
		twice = 0
		three = 0
		for item in A:
			twice = item & once
			once = once ^ item
			three = twice & once
			once = once & ~three
			twice = twice & ~ three

		return once
		 



if __name__ == '__main__':
	time1=time.time()
	data =  Solution1().singleNumber([1,2,3,1,2,3,1,2,3,5])
	time2 = time.time()
	print "Time to find output: ",data, '  is :',time2-time1

	time1=time.time()
	data =  Solution2().singleNumber([1,2,3,1,2,3,1,2,3,5])
	time2 = time.time()
	print "Time to find output: ",data, '  is :',time2-time1

	time1=time.time()
	data =  Solution3().singleNumber([1,2,3,1,2,3,1,2,3,5])
	time2 = time.time()
	print "Time to find output: ",data, '  is :',time2-time1

	time1=time.time()
	data =  Solution4().singleNumber([1,2,3,1,2,3,1,2,3,5])
	time2 = time.time()
	print "Time to find output: ",data, '  is :',time2-time1

	time1=time.time()
	data =  Solution5().singleNumber([1,2,3,1,2,3,1,2,3,5])
	time2 = time.time()
	print "Time to find output: ",data, '  is :',time2-time1

