def linear_search(arr,target):
    n = len(arr)
    found=True
    idx = 0
    for i in range(0,n):
        if(arr[i]==target):
            found = True
            idx = i
            break
        else:
            found = False
    if(found == True):
        print(f"Target element found at {idx}th index!")
    else:
        print("Target element not found")

arr = [3,6,5,9,1,15,8]
linear_search(arr,1)        
linear_search(arr,20)