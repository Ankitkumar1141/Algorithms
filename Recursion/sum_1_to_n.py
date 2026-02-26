def calculate_sum(n):
    sum=0
    if(n==0):
        return 0
    sum=n + calculate_sum(n-1)
    return sum

print(calculate_sum(5))