def print_val(n):
    # Base Case
    if(n==0):
        return
    print(n)
    print_val(n-1)


print_val(7)