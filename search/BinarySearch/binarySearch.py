#recusrive binary search
def binarySearch(arr, low, high, find):

    if high >=low:
        mid = (high+low)//2

    #base case
        if arr[mid] == find:
            return mid
    
    #if find is smaller than mid, find is in the left subtree
        elif arr[mid]>find:
            return binarySearch(arr, low, mid-1, find)
    
    #if find is larger than mid, find is in the right subtree
        elif arr[mid]<find:
            return binarySearch(arr, mid+1, high, find)

    else:     
        return -1


if __name__ == "__main__":
    arr = [2,5,8,12,16,20,24,28,32,36,40,44,48,52]
    low = 0
    high = len(arr)-1
    find = 36
    result = binarySearch(arr, low, high, find)
    if result == -1:
        print("Element is not in the list")
    else:
        print("Element is present at the index "+ str(result))
    
    