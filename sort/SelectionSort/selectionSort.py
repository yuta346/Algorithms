
def selectionSort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min]:
                min = j     #update the index 
        if min != i:
            temp = arr[i]
            arr[i]=arr[min]
            arr[min]=temp

if __name__ == "__main__":
    arr = [14, 33, 27, 10, 35, 19, 42, 44, 3, 1, 95]
    selectionSort(arr)
    for i in arr:
        print(i)




