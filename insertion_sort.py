#!/usr/bin/env python
"""
Implementation of insertion sort on list in python

Ex:   4 2 7 1  0 5

1.     4    2          		  7 1  0 5 
         24                	  7 1  0 5 
2.       24      7              1  0 5 
3.          247                 1  0 5 
4.          247     1 			   0 5
                2477
                2447
                2247
                1247				0 5 

5. 				1247		0 		  5 
                
                12477
                12447
                12247
                11247
                01247				  5 

6. 				01247        5			
				012477

					012457


"""
import time
import random
import functools

def count_time(func):
	@functools.wraps(func)
	def wrap(*args, **kwargs):
		t1 = time.time()
		res = func(*args, **kwargs)
		t2 = time.time()
		print ('Time run function %s = %.10g'%(func.func_name, t2-t1))
		return res

	return wrap


@count_time
def insertionSort(a, type='increasing'):
	'''
	Complexity: simplest case: O(n)
				worst case: O(n^2)
	'''
	if type == 'increasing':
		return insertionSortIncreasing(a)
	else:
		return insertionSortDecreasing(a)

def insertionSortDecreasing(a):
	"""
	Arange cards in cards game by decreasing
	"""
	for i in range(1,len(a)):
		key = a[i]
		j = i-1
		while j>=0 and a[j] <key:
			a[j+1] = a[j]
			j= j -1

		a[j+1] = key
	return a


def insertionSortIncreasing(a):
	"""
	Arange cards in cards game by increasing
	"""
	for i in range(1,len(a)):
		key = a[i]
		j = i-1
		while j>=0 and a[j] >key:
			a[j+1] = a[j]
			j= j -1

		a[j+1] = key
	return a


if __name__ == '__main__':
	print ('Sort a random list with 10000 element')
	a = [random.randrange(1,1000000,1) for i in range(0,10000)]
	res = insertionSort(a,'decrease')
	# print ('new sorted a ='+str(res))




