#!/usr/bin/env python
import sys


def quicksort(arr):
	return quick(arr)

def quick(arr):
	if len(arr) > 1:
		arr, mock = sort(arr)
		arr[:mock] = quick(arr[:mock])
		arr[mock:] = quick(arr[mock:])

	return arr

def sort(arr):
	mock_mb = arr[-1]
	low = []
	hight = []
	for i in range(len(arr)-1):
		if arr[i] <= mock_mb:
			low.append(arr[i])
		else:
			hight.append(arr[i])

	res = low + [arr[-1]] + hight
	return res, len(low)


if __name__ == '__main__':
	arr = [int(i) for i in sys.argv[1:]]

	print arr
	print quicksort(arr)
