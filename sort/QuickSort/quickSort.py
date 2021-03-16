
def quickSort(arr, lb, ub):
    if(lb<ub):
        pindex = partition(arr, lb, ub)
        quickSort(arr, lb, pindex-1)
        quickSort(arr, pindex+1, ub)


def partition(arr, start, end):
    i = start-1
    pivot = arr[end]
    for j in range(start, end):
        if arr[j]<pivot:
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] #swap arr[i] and arr[j] 
  
    arr[i+1],arr[end] = arr[end],arr[i+1] #swap arr[i+1] and arr[end] 
    return ( i+1 ) 


if __name__ == "__main__":
    arr = [2, 6, 19, 1, 99, 39]
    start = 0
    end = len(arr)-1
    quickSort(arr, start, end)
    for i in arr:
        print(i)

         