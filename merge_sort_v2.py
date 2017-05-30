#!/usr/bin/python
import time
import random

def mergeSort(arr):
	if len(arr) == 1:
		return arr

	mid = len(arr)//2

	s1 = mergeSort(arr[0:mid])
	s2 = mergeSort(arr[mid:])

	arr = merge(s1, s2)
	return arr

def merge(s1, s2):
	res = []

	while s1 and s2:
		if s1[0] < s2[0]:
			res.append(s1[0])
			del s1[0]

		else:
			res.append(s2[0])
			del s2[0]

	if s1:
		res.extend(s1)
	else:
		res.extend(s2)

	return res




if __name__ == '__main__':
	print "Sort a random integer list"
	arr = [random.randrange(1,1000,1) for i in range(10)]

	time1 = time.time()
	res = mergeSort(arr)
	time2 = time.time()
	print 'time to run merge sort on list 1000 item: ' + str(time2-time1)



	# 2 4 1 6 89 0 4 8 0