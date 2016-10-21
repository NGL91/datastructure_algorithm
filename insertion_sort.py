#!/usr/bin/env python
import time
import functools

def count_time(func):
	@functools.wraps(func)
	def wrap(*args, **kwargs):
		t1 = time.time()
		res = func(*args, **kwargs)
		t2 = time.time()
		print ('Time run function %s = %.15f'%(func.func_name, t2-t1))
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
	a = [31,41,59,26,41,58]
	res = insertionSort(a,'decrease')
	print ('new sorted a ='+str(res))




