def factorial(n):
    prod=1
    if(n==1):
        return 1
    prod=n*factorial(n-1)
    return prod

print(factorial(5))