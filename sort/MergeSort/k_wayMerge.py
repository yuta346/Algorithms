import random
import heapq
def generate(nrange = 1000, quantity = 5):
	if nrange < quantity:
		nrange = quantity

	rnumbers = list(range(nrange))
	rlist = list()
	for _ in range(quantity):
		pick = random.randint(0, len(rnumbers)-1)
		rlist.append(rnumbers[pick])
		rnumbers.pop(pick)
	rlist.sort()
	return rlist
li = []
for i in range(25):
	li.append(generate())

#k-way merge sort using naive direct method
def merge_sort(arr):
	if len(arr)<=1:
		return 
	num_array = len(arr)       
	result_list = merge(arr[0], arr[1])   
	print("First Result list",result_list)
	for i in range(2,num_array):
		result_list = merge(result_list, arr[i])
		print("{} Result list".format(i),result_list)
	return result_list

def merge(left,right):
	sorted_list = []
	len_left = len(left)
	len_right = len(right)
	i = j =  0
	while i<len_left and j<len_right:
		if left[i]<=right[j]:
			sorted_list.append(left[i])
			i+=1
		else:
			sorted_list.append(right[j])
			j+=1
	while i<len_left :
		sorted_list.append(left[i])
		i+=1

	while j<len_right :
		sorted_list.append(right[j])
		j+=1
	return sorted_list
		

#k-way merge using priority queue
def mergeKArray(li):
	priority_queue = []
	result = []
	for arr in li:
		for num in arr:
			heapq.heappush(priority_queue, num)
	while priority_queue:
		min = heapq.heappop(priority_queue)
		result.append(min)
	return result



if __name__ == "__main__":
	lists= [[4, 6, 8], [1, 2, 23], [7, 98, 99], [5, 10, 15]]
	print("The original arr is:",lists)
	print(merge_sort(lists))
	print("The sorted arr is:", merge_sort(lists))
	print("K-way Sorted Array",mergeKArray(lists))