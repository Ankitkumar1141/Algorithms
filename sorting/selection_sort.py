def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min = arr[i]
        min_idx = i
        for j in range(i+1,n):
            if (arr[j] < min):
                min = arr[j]
                min_idx = j
        # swap
        temp = arr[min_idx]
        arr[min_idx] = arr[i]
        arr[i] = temp
    return arr

arr = [5,4,3,2,1]
print("Unsorted array",end=": ")
print(arr)
print("Sorted array",end=": ")
print(selection_sort(arr))
print(selection_sort(arr))