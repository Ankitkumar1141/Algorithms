def print_val(n):
    if(n==0):
        return
    print_val(n-1)
    print(n)

print_val(7)