#!/usr/bin/en python
"""
Implementation of quick sort
"""

from insertion_sort import count_time
import random

@count_time
def quick_sort(a, type='increasing'):
	return quick_sort_increasing(a, 0 , len(a)-1)

def quick_sort_increasing(a, left, right):
	if left < right:
		a, pivot= partitionFunc(a, left, right)
		a= quick_sort_increasing(a, left, pivot-1)
		a = quick_sort_increasing(a, pivot+1, right)

	return a

def partitionFunc(a, start, end):
	pivot = a[start]
	left = start +1
	right = end 
	while True:
		while right >= left and a[right] >= pivot:
			right -=1

		while left <= right and a[left] <= pivot:
			left +=1


		if left > right:
			break
		else:
			a[left], a[right] = a[right], a[left]

	a[right],a[start] = a[start],a[right]
	return a, right



if __name__ == '__main__':
	print ('Sort a random list with 10000 element')
	a = [random.randrange(1,1000000,1) for i in range(0,10000)]
	res = quick_sort(a)
	# print ('new sorted a ='+str(res))