
def linearSearch(arr, target):
    found = False
    for i in range(len(arr)):
        if arr[i]==target:
            print("Element is present at index: "+ str(i))
            found = True
            break
    if found == False:
        print("Element is not in the list")



if __name__ == "__main__":
    arr = [5, 7, 16, 28, 39, 48, 52, 65, 78]
    target = 7
    linearSearch(arr, target)