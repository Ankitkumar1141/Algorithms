def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i
        while(j>0 and arr[j] < arr[j-1]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
    return arr

arr = [7,5,3,2]
print("Unsorted array",end=": ")
print(arr)
print("Sorted array",end=": ")
print(insertion_sort(arr))