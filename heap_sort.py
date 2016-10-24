#!/usr/bin/env python
"""
Implementation of heap sort on a  random list

Step 1:  Create max heap (value at each node is larger than child node)
Step 2: Swap between node at first and last list
Step 3: Continue create max heap

Loop step 2 and 3 until remain list to make max heap has one element

Heap sort = combine of insertion sort and merge sort
       Inplace list
       Complexity = merge sort
"""
from insertion_sort import count_time
import random



@count_time
def heap_sort(a):
	"""
		Complexity: O(nlog(n))
	"""
	length = len(a)
	for i in range(length-1, -1, -1):
		heaptify(a, length, i)

	for i in range(length-1, 0, -1):
		a[i],a[0] = a[0],a[i]
		#Make sure that parent node is larger than all childs node
		heaptify(a, i, 0)


	return a



def heaptify(a, n, i):
	largest = i
	left = i*2+1
	right = i*2+2

	if left < n and a[left] > a[largest]:
		largest = left

	if right < n and a[right] > a[largest]:
		largest = right

	if largest != i:
		a[largest],a[i] = a[i],a[largest]
		heaptify(a, n, largest)




if __name__ == '__main__':
	print ('Sort a random list with 10000 element')
	a = [random.randrange(1,1000000,1) for i in range(0,10000)]
	res = heap_sort(a)
	# print ('new sorted a ='+str(res))