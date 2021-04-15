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
print("K-way Sorted Array",mergeKArray(li))