#!/usr/bin/env python
import sys


def mergesortFunc(arr):
	start = 0
	end = len(arr)-1
	arr = mergesort(arr)
	return arr

def mergesort(arr):
	if len(arr) > 1:
		middle = len(arr)/2
		arr[:middle] = mergesort(arr[:middle])
		arr[middle:] = mergesort(arr[middle:])
		arr = merge(arr, middle)

	return arr

def merge(arr, middle):
	c1 = arr[:middle]
	c2 = arr[middle:]

	start = 0
	end = middle+1
	res = []
	while len(c1) and len(c2):
		if c1[0] <= c2[0]:
			res.append(c1[0])
			del c1[0]
		else:
			res.append(c2[0])
			del c2[0]

	if c1:
		res.extend(c1)
	else:
		res.extend(c2)

	return res





if __name__ == '__main__':
	arr = sys.argv[1:]
	arr=[int(item) for item in arr]
	print arr
	print mergesortFunc(arr)