
def quickSort(lists):
	return quickSortAsc(lists, 0, len(lists)-1)

def quickSortAsc(lists, left, right):
	if left < right:
		lists, pivot = partitionFunc(lists, left, right)
		lists = quickSortAsc(lists, 0, pivot-1)
		lists = quickSortAsc(lists, pivot+1, right)
	return lists

def partitionFunc(lists, left, right):
	pivot = left
	left += 1
	while True:
		while left <= right and lists[left] <= lists[pivot]:
			left +=1

		while left <= right and lists[right] >= lists[pivot]:
			right -=1

		if left > right:
			break
		else:
			lists[left], lists[right] = lists[right], lists[left]

	lists[pivot], lists[right] = lists[right], lists[pivot]

	return lists, right







if __name__ == '__main__':
	print quickSort([1,3,5,1,7,8,6,2])