import math
def jumpSearch( arr , x , n ):
	step = math.sqrt(n)
	prev = 0
	while arr[int(min(step, n)-1)] < x:
		prev = step
		step += math.sqrt(n)
		if prev >= n:
			return -1
	while arr[int(prev)] < x:
		prev += 1
		if prev == min(step, n):
			return -1
	if arr[int(prev)] == x:
		return prev
	
	return -1

arr = [ 0, 1, 1, 2, 3, 3, 8, 13, 21,
	34, 55, 89, 144, 233, 377, 610 ]
x = 5
n = len(arr)


index = jumpSearch(arr, x, n)

if(int(index)==-1):
	print("Number" , x, "not found in the array");
else:
  print("Number" , x, "is at index" ,int(index))
