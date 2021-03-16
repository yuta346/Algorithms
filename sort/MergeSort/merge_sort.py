def merge_sort(arr):
	if len(arr)<=1:
		return 
	mid = len(arr)//2
	left = arr[:mid]
	right = arr[mid:]
	merge_sort(left)
	merge_sort(right)
	merge(left,right,arr)
	
def merge(left,right,arr):
	len_left = len(left)
	len_right = len(right)
	i = j = k = 0
	while i<len_left and j<len_right:
		if left[i]<=right[j]:
			arr[k]=left[i]
			i+=1
		else:
			arr[k]=right[j]
			j+=1
		k+=1
	while i<len_left :
		arr[k]=left[i]
		i+=1
		k+=1

	while j<len_right :
		arr[k]=right[j]
		j+=1
		k+=1
if __name__ == "__main__":
	arr= [10, 3, 15, 7, 8, 23, 98, 29]
	print("The original arr is:",arr)
	merge_sort(arr)
	print("The sorted arr is:", arr)
