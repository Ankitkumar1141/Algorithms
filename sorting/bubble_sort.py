def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

## Optimised
def bubble_sort2(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if(arr[j] > arr[j+1]):
                temp = arr[j] 
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

## More optimised
def bubble_sort3(arr):
    n = len(arr)
    for i in range(0,n-1):
        swap = False
        for j in range(0,n-1-i):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap = True
        if swap == False:
            print("Already sorted")
            break
    return arr

arr = [5,4,3,2,1]
print("Unsorted array",end=":  ")
print(arr)
print("Sorted array",end=": ")
print(bubble_sort3(arr))

print(bubble_sort3(arr))