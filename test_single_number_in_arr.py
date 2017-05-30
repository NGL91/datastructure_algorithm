def singleNumber(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	start = 0
	end = len(nums)-1

	while end > start :
	    mock = end
	    nums, new_mock_pos = quicksort(nums, mock, start, end)
	    #both partition is even==> mock is output
	    length_right = len(nums[start:new_mock_pos])
	    print nums[start:new_mock_pos]
	    if length_right %2 ==0:
		if length_right >0:
		   return nums[new_mock_pos]
		else:
		   end = new_mock_pos

	    else:
		start = new_mock_pos+1

	return nums[0]

def quicksort(nums, mock, start, end):
	check = end -1
	mock_number = nums[mock]
	while check >= start:
	    if nums[check] > mock_number:
		nums.append(nums[check])
		del nums[check]
		mock -=1
	    check -=1
	
	print "nums after sort"
	print nums
	return nums, mock

a=[1,2,2]
print singleNumber(a)
