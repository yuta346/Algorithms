
def bubbleSort(arr):
    for i in range(len(arr)-1): 
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1]=temp
                print(arr)
            
if __name__ == "__main__":
    #arr = [14, 33, 27, 67, 10, 140, 35, 19, 42, 44, 3, 1, 95]
    arr = [7,3,6,1,4,2,5,8]
    bubbleSort(arr)
    for i in arr:
        print(i)

