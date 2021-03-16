
def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1]=temp

if __name__ == "__main__":
    arr = [14, 33, 27, 10, 35, 19, 42, 44, 3, 1, 95]
    insertionSort(arr)
    for i in arr:
        print(i)