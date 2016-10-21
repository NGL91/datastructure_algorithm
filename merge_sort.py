#! /usr/bin/env python
"""
Implementation of Mert sort algorithm on a random list in python


Ex:     4 5 1 6 7 8 9 3 1

1.      4    5      1    6    7   8    9  3   1
2.       45        16          78        93   1
3.           1456                    3789      1
4.                     13456789                1
5.                                113456789


"""
from insertion_sort import count_time
import random

@count_time
def merge_sort(a, type='increasing'):
	return merge_sort_increasing(a)


def merge_sort_increasing(a):
	"""
	Merge sort combines smaller sorted lists keeping the new list sorted too.
	Complexity: O(nlog(n))
	"""
	if len(a)==1:
		return a

	s1 = a[:len(a)//2]
	s2 = a[len(a)//2:]
	s1 = merge_sort_increasing(s1)
	s2 = merge_sort_increasing(s2)

	a = merge(s1, s2)
	return a

def merge(s1, s2):
	c = []

	while s1 and s2:
		if s1[0] > s2[0]:
			c.append(s2[0])
			del s2[0]
		else:
			c.append(s1[0])
			del s1[0]

	if s1:
		c.extend(s1)

	elif s2:
		c.extend(s2)

	return c




if __name__ == '__main__':
	print ('Sort a random list with 10000 element')
	a = [random.randrange(1,100,1) for i in range(0,10000)]
	res = merge_sort(a)
	# print ('new sorted a ='+str(res))