def searchForRange(array, target):
	if len(array) == 0:
		return [-1,-1]
	beg, end = 0, len(array) - 1 
	while beg <= end:
		if target < array[beg] or target > array[end]:
			return [-1,-1]
		mid = (beg + end) // 2 
		print(mid, array[mid])
		if array[mid] == target:
			if array[mid-1] == target and array[mid + 1] == target:
				if array[beg] == target and array[end] == target:
					return [beg, end]
				elif array[beg] == target: 
					end -= 1
				elif array[end] == target:
					beg += 1
				else:
					print("reached")
					beg += 1
					end -= 1
			elif beg <= mid - 1 and array[mid-1] == target: #value after the mid doesnt equal target
				end = mid
			elif mid + 1 <= end and array[mid + 1] == target: #value before mid doesn't equal target
				beg = mid
			else:
				return [mid,mid]
		elif array[mid] < target:
			beg = mid + 1
		else:
			end = mid - 1
	return [-1,-1] if array[beg] != target else [beg,beg]
arr = [5, 7, 7, 8, 8, 10]
val = 8
print(searchForRange(arr,val))

#[0,1,21,33,45,45,45,45,45,45,61,71,73]